from fastapi import APIRouter
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel
from typing import Optional
import numpy as np
import pandas as pd
from tqdm import tqdm
import os

from app.schemas.matches import Events, Player

router = APIRouter()
# match_id = 2057988
match_events = pd.read_csv('./matches/KOR.GER/match_events.csv')
phase_records = pd.read_csv('./matches/KOR.GER/phase_records.csv')
all_player_stats = pd.read_csv('./matches/KOR.GER/matches_player_stats.csv')

# 이벤트 데이터를 시간에 따라 필터링
def filter_by_time(match_events, start_time=None, end_time=None):
    # Set the default values
    if start_time is None:
        start_time = match_events['time'].min()
    if end_time is None:
        end_time = match_events['time'].max()
    
    # Convert time to minutes
    match_events['time'] = match_events['time'] / 60

    # Filter the events
    filtered_events = match_events[(match_events['time'] >= start_time) & (match_events['time'] <= end_time)]
    
    return filtered_events

# 현재 시간에 출전 중인 선수들의 목록을 반환
@router.get("/lineup")
def read_teams(current_time: Optional[int] = None):
    # If current_time is not specified, return all players
    if current_time is None:
        team1_players = match_events[match_events['team_id'] == match_events['team_id'].unique()[0]]['player_name'].unique().tolist()
        team2_players = match_events[match_events['team_id'] == match_events['team_id'].unique()[1]]['player_name'].unique().tolist()
    else:
        # Identify the phase corresponding to the current time
        current_phase = phase_records[
            (phase_records['start_time'] <= current_time * 60) & 
            (phase_records['end_time'] > current_time * 60)
        ].iloc[0]

        # Filter the players who are on the field during the current phase
        team1_players = match_events[
            (match_events['team_id'] == match_events['team_id'].unique()[0]) & 
            (match_events['player_id'].isin(current_phase['player_ids']))
        ]['player_name'].unique().tolist()

        team2_players = match_events[
            (match_events['team_id'] == match_events['team_id'].unique()[1]) & 
            (match_events['player_id'].isin(current_phase['player_ids']))
        ]['player_name'].unique().tolist()

    teams = {
        match_events['team_id'].unique()[0]: team1_players,
        match_events['team_id'].unique()[1]: team2_players
    }
    
    return teams

# 경기 이벤트 데이터를 데이터에 따라 필터링하여 반환
@router.get("/events")
def filter_events(Evnets: Events):
    # Start with all events
    filtered = filter_by_time(match_events, start_time=Evnets.start_time, end_time=Evnets.end_time)
    
    # Apply filters if they are not None
    if Evnets.player_name is not None:
        filtered = filtered[filtered['player_name'] == Evnets.player_name]
    if Evnets.event_type is not None:
        filtered = filtered[filtered['event_type'] == Evnets.event_type]
    if Evnets.sub_event_type is not None:
        filtered = filtered[filtered['sub_event_type'] == Evnets.sub_event_type]
    if Evnets.team_name is not None:
        filtered = filtered[filtered['team_name'] == Evnets.team_name]
    if Evnets.tags is not None:
        filtered = filtered[filtered['tags'].apply(lambda x: Evnets.tags in x)]
    
    return filtered.to_dict('records')

# 경기 통계 데이터(골, 도움 등 각종 스텟들)를 시간대에 따라 반환
@router.get("/stats")
def generate_player_stats(current_time: Optional[int] = None):
    # Data loading
    filtered_events = filter_by_time(match_events, start_time=0, end_time=current_time * 60)
    filtered_events = filtered_events[filtered_events['period'] != 'P']

    # Goal stats
    goal_records = filtered_events[filtered_events['tags'].apply(lambda x: 'Goal' in x)]
    goals = goal_records.groupby(['team_id', 'team_name', 'player_id', 'player_name'])['event_id'].count()
    goals.name = 'goals'

    own_goal_records = filtered_events[filtered_events['tags'].apply(lambda x: 'Own goal' in x)]
    own_goals = own_goal_records.groupby(['team_id', 'team_name', 'player_id', 'player_name'])['event_id'].count()
    own_goals.name = 'own_goals'

    assist_records = filtered_events[filtered_events['tags'].apply(lambda x: 'Assist' in x)]
    assists = assist_records.groupby(['team_id', 'team_name', 'player_id', 'player_name'])['event_id'].count()
    assists.name = 'assists'

    goal_stats_list = [goals, assists, own_goals]
    goal_stats = pd.concat(goal_stats_list, axis=1).fillna(0).astype(int)

    # Shot stats
    shot_records = filtered_events[
        (filtered_events['event_type'] == 'Shot') |
        (filtered_events['sub_event_type'].isin(['Free kick shot', 'Penalty']))
    ]
    shots = shot_records.groupby(['team_id', 'team_name', 'player_id', 'player_name'])['event_id'].count()
    shots.name = 'total_shots'

    acc_shot_records = shot_records[shot_records['tags'].apply(lambda x: 'Accurate' in x)]
    acc_shots = acc_shot_records.groupby(['team_id', 'team_name', 'player_id', 'player_name'])['event_id'].count()
    acc_shots.name = 'shots_on_target'

    rshot_records = shot_records[shot_records['tags'].apply(lambda x: 'Right foot' in x)]
    rshots = rshot_records.groupby(['team_id', 'team_name', 'player_id', 'player_name'])['event_id'].count()
    rshots.name = 'rfoot_shots'

    lshot_records = shot_records[shot_records['tags'].apply(lambda x: 'Left foot' in x)]
    lshots = lshot_records.groupby(['team_id', 'team_name', 'player_id', 'player_name'])['event_id'].count()
    lshots.name = 'lfoot_shots'

    hshot_records = shot_records[shot_records['tags'].apply(lambda x: 'Head/body' in x)]
    hshots = hshot_records.groupby(['team_id', 'team_name', 'player_id', 'player_name'])['event_id'].count()
    hshots.name = 'header_shots'

    shot_stats_list = [shots, acc_shots, rshots, lshots, hshots]
    shot_stats = pd.concat(shot_stats_list, axis=1).fillna(0).astype(int)

    # Foul stats
    foul_records = filtered_events[filtered_events['event_type'] == 'Foul']
    fouls = foul_records.groupby(['team_id', 'team_name', 'player_id', 'player_name'])['event_id'].count()
    fouls.name = 'fouls'

    offside_records = filtered_events[filtered_events['event_type'] == 'Offside']
    offsides = offside_records.groupby(['team_id', 'team_name', 'player_id', 'player_name'])['event_id'].count()
    offsides.name = 'offsides'

    yellow_records = foul_records[foul_records['tags'].apply(lambda x: 'Yellow card' in x)]
    yellows = yellow_records.groupby(['team_id', 'team_name', 'player_id', 'player_name'])['event_id'].count()
    yellows.name = 'yellow_cards'

    red_records = foul_records[foul_records['tags'].apply(lambda x: 'Red card' in x)]
    reds = red_records.groupby(['team_id', 'team_name', 'player_id', 'player_name'])['event_id'].count()
    reds.name = 'red_cards'

    foul_stats = pd.concat([fouls, offsides, yellows, reds], axis=1).fillna(0).astype(int)

    # Pass stats
    pass_records = filtered_events[
        (filtered_events['event_type'] == 'Pass') |
        (filtered_events['sub_event_type'].isin(['Free kick', 'Free kick cross', 'corner']))
    ]
    passes = pass_records.groupby(['team_id', 'team_name', 'player_id', 'player_name'])['event_id'].count()
    passes.name = 'total_passes'

    acc_pass_records = pass_records[pass_records['tags'].apply(lambda x: 'Accurate' in x)]
    acc_passes = acc_pass_records.groupby(['team_id', 'team_name', 'player_id', 'player_name'])['event_id'].count()
    acc_passes.name = 'acc_passes'

    pass_stats = pd.concat([passes, acc_passes], axis=1).fillna(0).astype(int)
    pass_stats['pass_accuracy'] = (pass_stats['acc_passes'] / pass_stats['total_passes']).round(2)

    # Playing time
    player_change_records = filtered_events[
        (filtered_events['event_type'] == 'Substitution') |
        (filtered_events['tags'].apply(lambda x: 'Red card' in x))
    ]
    in_players = player_change_records[player_change_records['sub_event_type'] == 'Player in']['player_id'].tolist()
    player_ids = [p for p in filtered_events['player_id'].unique() if not p in in_players]

    period_durations = filtered_events.groupby('period')['time'].max()
    phase_record_list = []
    phase = 1

    for period in period_durations.index:
        change_times = player_change_records[player_change_records['period'] == period]['time'].unique().tolist()
        change_times.append(period_durations[period])
        if 0 not in change_times:
            change_times = [0] + change_times

        for i in range(len(change_times[:-1])):
            moment_records = player_change_records[
                (player_change_records['period'] == period) &
                (player_change_records['time'] == change_times[i])
            ]

            for _, record in moment_records.iterrows():
                if record['sub_event_type'] == 'Player out' or record['event_type'] == 'Foul':
                    player_ids.remove(record['player_id'])
                else:
                    player_ids.append(record['player_id'])

            phase_record = {
                'phase': phase,
                'period': period,
                'start_time': change_times[i],
                'end_time': change_times[i+1],
                'duration': change_times[i+1] - change_times[i],
                'player_ids': player_ids.copy()
            }
            phase += 1

            phase_record_list.append(phase_record)

    phase_records = pd.DataFrame(phase_record_list).set_index('phase')

    player_ids = np.sort(filtered_events['player_id'].unique())
    for player_id in player_ids:
        phase_records[player_id] = 0

    for phase in phase_records.index:
        for player_id in phase_records.at[phase, 'player_ids']:
            phase_records.at[phase, player_id] = 1

    phase_records = phase_records[np.concatenate([phase_records.columns[:4], player_ids])]

    playing_times = pd.Series(index=player_ids, dtype='float')
    for player_id in player_ids:
        playing_times[player_id] = phase_records[phase_records[player_id] == 1]['duration'].sum().round(1)
    playing_times = playing_times.reset_index()
    playing_times.columns = ['player_id', 'playing_time']

    # Concatenation
    player_stats = pd.concat([goal_stats, shot_stats, foul_stats, pass_stats], axis=1, sort=True).fillna(0)
    for col in player_stats.columns:
        if col != 'pass_accuracy':
            player_stats[col] = player_stats[col].astype(int)

    player_stats = pd.merge(player_stats.reset_index(), playing_times)

    cols = player_stats.columns.tolist()
    cols = cols[:4] + ['playing_time'] + cols[4:-2]
    return player_stats[cols]

# 대회 선수들 통계 합산 반환 -> TOP 10까지 반환 및 특정 선수 통계 반환
@router.get("/group")
async def read_top10_players(Player: Player):
    grouped = all_player_stats.groupby(['team_id', 'team_name', 'player_id', 'player_name'])

    player_stats_accum = grouped[all_player_stats.columns[5:-1]].sum()
    player_stats_accum['pass_accuracy'] = (player_stats_accum['acc_passes'] / player_stats_accum['total_passes']).round(2)
    player_stats_accum['matches'] = grouped['match_id'].count()

    player_stats_accum = player_stats_accum[['matches'] + all_player_stats.columns[5:-1].tolist()].reset_index()

    # If stats is provided, sort by stats and take top 10
    if Player.stats:
        data = player_stats_accum.sort_values(Player.stats, ascending=False).head(10)
    else:
        data = player_stats_accum.head(10) # Modify this if you want to sort by a default column

    # If player_name is provided and not in top 10, append player's row
    if Player.player_name and Player.player_name not in data['player_name'].values:
        player_row = player_stats_accum[player_stats_accum['player_name'] == Player.player_name]
        data = pd.concat([data, player_row])
    
    return data.to_dict()

# 특정 선수에 대한 이전 경기 기록 반환
@router.get("/player/{player_name}")
async def read_player(player_name: str):
    # Filter the data by player_name
    data = all_player_stats[all_player_stats['player_name'] == player_name]

    return data.to_dict()