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
seq_records = pd.read_csv('./matches/KOR.GER/seq_records.csv')
match_shots = pd.read_csv('./matches/KOR.GER/match_shots.csv')

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

# 이벤트 데이터 인덱스를 기반으로 공격 시퀀스 검출
def detect_attack_sequences(match_events, first_idx, last_idx):
    cols = [
        'period', 'time', 'display_time', 'team_name', 'player_name',
        'event_type', 'sub_event_type', 'tags', 'start_x', 'start_y', 'end_x', 'end_y'
    ]
    match_events = match_events[match_events['event_type'] != 'Substitution'][cols]

    seq_events = match_events.loc[first_idx:last_idx].copy()
    seq_events[seq_events.columns[2:-4]]

    return seq_events[seq_events.columns[2:-4]]

# 현재 시간에 가장 가까운 이벤트 인덱스 반환
def find_nearest_event(current_time: int):
    # Calculate the absolute difference between current time and event times
    time_diff = abs(match_events['time'] - current_time)
    
    # Find the index of the minimum difference
    nearest_event_index = time_diff.idxmin()
    
    return nearest_event_index

# 인덱스를 포함하고 있는 sequence의 column을 반환
def find_sequence(index: int):
    # Iterate over all columns of seq_records
    for column in seq_records.columns:
        # Check if the index is within the range of first_idx and last_idx of the current column
        if seq_records[column]['first_idx'] <= index <= seq_records[column]['last_idx']:
            return column
    return "Index not found in any column"

# 현재 시간에 출전 중인 선수들의 목록을 반환
@router.get("/lineup")
def read_teams(current_time: Optional[int] = None):
    # If current_time is not specified, return all players
    if current_time is None:
        team1_players = match_events[match_events['team_id'] == match_events['team_id'].unique()[0]]['player_name'].unique().tolist()
        team2_players = match_events[match_events['team_id'] == match_events['team_id'].unique()[1]]['player_name'].unique().tolist()
    else:
        # Identify the phase corresponding to the current time
        # 클라이언트에서 current_time이 어떻게 넘어오는지 확인 필요
        # current_time에 따라 period를 구분해야 함
        # 예를 들어 current_time이 45 이상 일 때, period를 2로 설정하고 current_time에서 45를 빼줘야 함
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
def read_top10_players(Player: Player):                         
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
def read_player(player_name: str):
    # Filter the data by player_name
    data = all_player_stats[all_player_stats['player_name'] == player_name]

    return data.to_dict()

# 공격 시퀀스 데이터 반환
@router.get("/sequence")
def read_sequence(current_time: int):
    
    # 현재 시간 기준 가장 가까운 이벤트 찾기
    nearest_event_index = find_nearest_event(current_time)

    # 인덱스를 포함하는 시퀀스 찾기
    sequence = find_sequence(nearest_event_index)

    first_idx, last_idx = sequence['first_idx'], sequence['last_idx'] 

    # 시퀀스 데이터 검출
    attack_sequence = detect_attack_sequences(match_events, first_idx, last_idx)

    # 프론트엔드에서 어떻게 시각화 하느냐에 따라 attack_sequence의 형태를 바꿔야 함
    return attack_sequence

# 기대득점 데이터 반환
@router.get("/match_shots")
async def get_match_shots(current_time: int):
    # Process the data
    match_shots = filter_by_time(match_shots, end_time=current_time)

    match_shots_failed = match_shots[match_shots['tags'].apply(lambda x: 'Goal' not in x)]
    team1_name, team2_name = match_shots['team_name'].unique()

    team1_shots = match_shots[match_shots['team_name'] == team1_name]
    team2_shots = match_shots[match_shots['team_name'] == team2_name]

    team1_goals = team1_shots[team1_shots['tags'].apply(lambda x: 'Goal' in x)]
    team2_goals = team2_shots[team2_shots['tags'].apply(lambda x: 'Goal' in x)]

    # Create the JSON response
    response = {
        "team1": {
            "name": team1_name,
            "goals": team1_goals[['x', 'y', 'display_name', 'xg', 'freekick']].to_dict(orient='records'),
            "xg": team1_shots['xg'].sum().round(2)
        },
        "team2": {
            "name": team2_name,
            "goals": team2_goals[['x', 'y', 'display_name', 'xg', 'freekick']].to_dict(orient='records'),
            "xg": team2_shots['xg'].sum().round(2)
        },
        "failed_shots": match_shots_failed[['x', 'y', 'display_name', 'xg', 'freekick']].to_dict(orient='records')
    }

    return response

# 세트 피스 데이터 반환
@router.get("/setpieces")
def get_setpieces(current_time: int):
    # Filter the data by time
    match_events = filter_by_time(match_events, end_time=current_time)

    # Filter out the set-piece situations
    set_piece_events = match_events[match_events['sub_event_type'].isin(['Corner', 'Free Kick'])]

    # Sort the events in chronological order
    set_piece_events_sorted = set_piece_events.sort_values(['period', 'time'])
    return set_piece_events_sorted.to_dict(orient='records')