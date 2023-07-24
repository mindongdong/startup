from fastapi import APIRouter
from typing import Optional
import numpy as np
import pandas as pd
import ast
from app.schemas.matches import Events, Player

router = APIRouter()
# match_id = 2057988
match_events = pd.read_csv('./matches/KOR.GER/match_events_korean_final.csv')
phase_records = pd.read_csv('./matches/KOR.GER/phase_records_korean_sorted.csv')
all_player_stats = pd.read_csv('./matches/KOR.GER/matches_player_stats_korean.csv')
seq_records = pd.read_csv('./matches/KOR.GER/seq_records.csv')
match_shots = pd.read_csv('./matches/KOR.GER/match_shots_korean_final.csv')

def filter_by_time(match_events, start_time=None, end_time=None):
    # Set the default values
    if start_time is None:
        start_time = match_events['time'].min()
    if end_time is None:
        end_time = match_events['time'].max()

    # Determine the period and adjust the times if necessary
    if end_time >= 2882:
        period = '2H'
        end_time -= 2882
    else:
        period = '1H'

    # print("start_time:", start_time)
    # print("end_time:", end_time)
    # print("period:", period)

    # Filter the events
    if period == '2H':
        # If the period is '2H', include all events from '1H' plus those from '2H' within the specified times
        filtered_events = pd.concat([
            match_events[match_events['period'] == '1H'],
            match_events[(match_events['period'] == '2H') & (match_events['time'] >= start_time) & (match_events['time'] <= end_time)]
        ])
    else:
        # If the period is not '2H', filter as usual
        filtered_events = match_events[(match_events['period'] == period) & (match_events['time'] >= start_time) & (match_events['time'] <= end_time)]
    
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
@router.get("/lineup/{current_time}")
def get_teams(current_time: float = None):
    # If current_time is None, return an empty dictionary
    if current_time is None:
        return {}
    
    # Filter rows where current_time is between start_time and end_time
    filtered_data = phase_records[(phase_records['start_time'] <= current_time) & (phase_records['end_time'] > current_time)]
    
    # Initialize an empty dictionary
    teams = {}
    
    # Iterate over filtered rows
    for _, row in filtered_data.iterrows():
        # Convert string representation of list to actual list
        player_names = ast.literal_eval(row['player_names'])
        # Add to dictionary
        teams[row['team_name']] = player_names
        
    return teams


# 경기 이벤트 데이터를 데이터에 따라 필터링하여 반환
@router.post("/events")
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
@router.get("/stats/{current_time}")
def generate_player_stats(current_time: float):
    # Data loading
    filtered_events = filter_by_time(match_events, end_time=current_time)
    # print(filtered_events)

    # Goal stats
    try:
        goal_records = filtered_events[(filtered_events['tags'].apply(lambda x: 'Goal' in x.split(','))) & (filtered_events['event_type'] == 'Shot')]
        if not goal_records.empty:
            goals = goal_records.groupby(['team_id', 'team_name', 'player_id', 'player_name'])['event_id'].count()
            goals.name = 'goals'
        else:
            goals = pd.Series(dtype='int')
            goals.name = 'goals'
    except KeyError:
        goals = pd.Series(dtype='int')
        goals.name = 'goals'

    try:
        own_goal_records = filtered_events[filtered_events['tags'].apply(lambda x: 'Own goal' in x)]
        if not own_goal_records.empty:
            own_goals = own_goal_records.groupby(['team_id', 'team_name', 'player_id', 'player_name'])['event_id'].count()
            own_goals.name = 'own_goals'
        else:
            own_goals = pd.Series(dtype='int')
            own_goals.name = 'own_goals'
    except KeyError:
        own_goals = pd.Series(dtype='int')
        own_goals.name = 'own_goals'

    try:
        assist_records = filtered_events[filtered_events['tags'].apply(lambda x: 'Assist' in x)]
        if not assist_records.empty:
            assists = assist_records.groupby(['team_id', 'team_name', 'player_id', 'player_name'])['event_id'].count()
            assists.name = 'assists'
        else:
            assists = pd.Series(dtype='int')
            assists.name = 'assists'
    except KeyError:
        assists = pd.Series(dtype='int')
        assists.name = 'assists'

    goal_stats_list = [goals, assists, own_goals]
    goal_stats = pd.concat(goal_stats_list, axis=1).fillna(0).astype(int)

    # Shot stats
    try:
        shot_records = filtered_events[
            (filtered_events['event_type'] == 'Shot') |
            (filtered_events['sub_event_type'].isin(['Free kick shot', 'Penalty']))
        ]
        if not shot_records.empty:
            shots = shot_records.groupby(['team_id', 'team_name', 'player_id', 'player_name'])['event_id'].count()
            shots.name = 'total_shots'
        else:
            shots = pd.Series(dtype='int')
            shots.name = 'total_shots'
    except KeyError:
        shots = pd.Series(dtype='int')
        shots.name = 'total_shots'

    try:
        acc_shot_records = shot_records[shot_records['tags'].apply(lambda x: 'Accurate' in x)]
        if not acc_shot_records.empty:
            acc_shots = acc_shot_records.groupby(['team_id', 'team_name', 'player_id', 'player_name'])['event_id'].count()
            acc_shots.name = 'shots_on_target'
        else:
            acc_shots = pd.Series(dtype='int')
            acc_shots.name = 'shots_on_target'
    except KeyError:
        acc_shots = pd.Series(dtype='int')
        acc_shots.name = 'shots_on_target'

    try:
        rshot_records = shot_records[shot_records['tags'].apply(lambda x: 'Right foot' in x)]
        if not rshot_records.empty:
            rshots = rshot_records.groupby(['team_id', 'team_name', 'player_id', 'player_name'])['event_id'].count()
            rshots.name = 'rfoot_shots'
        else:
            rshots = pd.Series(dtype='int')
            rshots.name = 'rfoot_shots'
    except KeyError:
        rshots = pd.Series(dtype='int')
        rshots.name = 'rfoot_shots'

    try:
        lshot_records = shot_records[shot_records['tags'].apply(lambda x: 'Left foot' in x)]
        if not lshot_records.empty:
            lshots = lshot_records.groupby(['team_id', 'team_name', 'player_id', 'player_name'])['event_id'].count()
            lshots.name = 'lfoot_shots'
        else:
            lshots = pd.Series(dtype='int')
            lshots.name = 'lfoot_shots'
    except KeyError:
        lshots = pd.Series(dtype='int')
        lshots.name = 'lfoot_shots'

    try:
        hshot_records = shot_records[shot_records['tags'].apply(lambda x: 'Head/body' in x)]
        if not hshot_records.empty:
            hshots = hshot_records.groupby(['team_id', 'team_name', 'player_id', 'player_name'])['event_id'].count()
            hshots.name = 'header_shots'
        else:
            hshots = pd.Series(dtype='int')
            hshots.name = 'header_shots'
    except KeyError:
        hshots = pd.Series(dtype='int')
        hshots.name = 'header_shots'

    shot_stats_list = [shots, acc_shots, rshots, lshots, hshots]
    shot_stats = pd.concat(shot_stats_list, axis=1).fillna(0).astype(int)

    # Foul stats
    try:
        foul_records = filtered_events[filtered_events['event_type'] == 'Foul']
        if not foul_records.empty:
            fouls = foul_records.groupby(['team_id', 'team_name', 'player_id', 'player_name'])['event_id'].count()
            fouls.name = 'fouls'
        else:
            fouls = pd.Series(dtype='int')
            fouls.name = 'fouls'
    except KeyError:
        fouls = pd.Series(dtype='int')
        fouls.name = 'fouls'

    try:
        offside_records = filtered_events[filtered_events['event_type'] == 'Offside']
        if not offside_records.empty:
            offsides = offside_records.groupby(['team_id', 'team_name', 'player_id', 'player_name'])['event_id'].count()
            offsides.name = 'offsides'
        else:
            offsides = pd.Series(dtype='int')
            offsides.name = 'offsides'
    except KeyError:
        offsides = pd.Series(dtype='int')
        offsides.name = 'offsides'

    try:
        yellow_records = foul_records[foul_records['tags'].apply(lambda x: 'Yellow card' in x)]
        if not yellow_records.empty:
            yellows = yellow_records.groupby(['team_id', 'team_name', 'player_id', 'player_name'])['event_id'].count()
            yellows.name = 'yellow_cards'
        else:
            yellows = pd.Series(dtype='int')
            yellows.name = 'yellow_cards'
    except KeyError:
        yellows = pd.Series(dtype='int')
        yellows.name = 'yellow_cards'

    try:
        red_records = foul_records[foul_records['tags'].apply(lambda x: 'Red card' in x)]
        if not red_records.empty:
            reds = red_records.groupby(['team_id', 'team_name', 'player_id', 'player_name'])['event_id'].count()
            reds.name = 'red_cards'
        else:
            reds = pd.Series(dtype='int')
            reds.name = 'red_cards'
    except KeyError:
        reds = pd.Series(dtype='int')
        reds.name = 'red_cards'

    foul_stats = pd.concat([fouls, offsides, yellows, reds], axis=1).fillna(0).astype(int)

    # Pass stats
    try:
        pass_records = filtered_events[
            (filtered_events['event_type'] == 'Pass') |
            (filtered_events['sub_event_type'].isin(['Free kick', 'Free kick cross', 'corner']))
        ]
        if not pass_records.empty:
            passes = pass_records.groupby(['team_id', 'team_name', 'player_id', 'player_name'])['event_id'].count()
            passes.name = 'total_passes'
        else:
            passes = pd.Series(dtype='int')
            passes.name = 'total_passes'
    except KeyError:
        passes = pd.Series(dtype='int')
        passes.name = 'total_passes'

    try:
        acc_pass_records = pass_records[pass_records['tags'].apply(lambda x: 'Accurate' in x)]
        if not acc_pass_records.empty:
            acc_passes = acc_pass_records.groupby(['team_id', 'team_name', 'player_id', 'player_name'])['event_id'].count()
            acc_passes.name = 'acc_passes'
        else:
            acc_passes = pd.Series(dtype='int')
            acc_passes.name = 'acc_passes'
    except KeyError:
        acc_passes = pd.Series(dtype='int')
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
    
    stat_event_types = {
        'key_passes': ('Pass', 'Smart pass', 'Accurate'),
        'interceptions': ('Duel', ['Ground defending duel', 'Ground loose ball duel'], 'Interception'),
        'tackle': ('Duel', ['Ground defending duel', 'Ground attacking duel'], None),
        'tackle_accuracy': ('Duel', ['Ground defending duel', 'Ground attacking duel'], 'Accurate'),
        'clearances': ('Others on the ball', 'Clearance', None)
    }

    # Calculate each statistic for each player
    for stat, (event_type, sub_event_types, tag) in stat_event_types.items():
        if isinstance(sub_event_types, list):
            player_stats[stat] = filtered_events[(filtered_events['event_type'] == event_type) & (filtered_events['sub_event_type'].isin(sub_event_types)) & (filtered_events['tags'].str.contains(tag) if tag else True)].groupby(['team_id', 'team_name', 'player_id', 'player_name'])['event_id'].count()
        else:
            player_stats[stat] = filtered_events[(filtered_events['event_type'] == event_type) & (filtered_events['sub_event_type'] == sub_event_types) & (filtered_events['tags'].str.contains(tag) if tag else True)].groupby(['team_id', 'team_name', 'player_id', 'player_name'])['event_id'].count()

    # Calculate the number of tackles and successful tackles for each player
    tackle_events = filtered_events[(filtered_events['event_type'] == 'Duel') & (filtered_events['sub_event_type'].isin(['Ground defending duel', 'Ground attacking duel']))]
    if not tackle_events.empty:
        player_stats['tackle'] = tackle_events.groupby(['team_id', 'team_name', 'player_id', 'player_name'])['event_id'].count()

    successful_tackle_events = tackle_events[tackle_events['tags'].str.contains('Accurate')]
    if not successful_tackle_events.empty:
        player_stats['successful_tackles'] = successful_tackle_events.groupby(['team_id', 'team_name', 'player_id', 'player_name'])['event_id'].count()

    # Calculate tackle accuracy as the probability of a successful tackle
    if 'tackle' in player_stats.columns and 'successful_tackles' in player_stats.columns:
        player_stats['tackle_accuracy'] = player_stats['successful_tackles'] / player_stats['tackle']

    # Re-calculate total saves and successful saves for each team (since there is only one goalkeeper in each team)
    team_stats = pd.DataFrame()
    save_attempt_events = filtered_events[filtered_events['event_type'] == 'Save attempt']
    if not save_attempt_events.empty:
        team_stats['total_saves'] = save_attempt_events.groupby('team_id')['event_id'].count()

    successful_save_attempt_events = save_attempt_events[save_attempt_events['tags'].str.contains('Accurate')]
    if not successful_save_attempt_events.empty:
        team_stats['successful_saves'] = successful_save_attempt_events.groupby('team_id')['event_id'].count()

    # Re-calculate total effective shots for each team
    shot_events = filtered_events[filtered_events['event_type'] == 'Shot']
    if not shot_events.empty:
        team_stats['effective_shots'] = shot_events.groupby('team_id')['event_id'].count()

    # Re-calculate save rate for each team
    if 'successful_saves' in team_stats.columns and 'effective_shots' in team_stats.columns:
        team_stats['save_rate'] = team_stats['successful_saves'] / team_stats['effective_shots']

    # Re-get the goalkeeper for each team
    if not save_attempt_events.empty:
        team_goalkeepers = save_attempt_events.groupby('team_id')['player_name'].first()

    # Initialize goalkeeper stats in player_stats
    player_stats['total_saves'] = 0
    player_stats['successful_saves'] = 0
    player_stats['save_rate'] = 0

    # Re-add the goalkeeper statistics to the player statistics
    if 'team_goalkeepers' in locals():
        for team, goalkeeper in team_goalkeepers.items():
            # Create a boolean mask for matching rows
            player_stats.index.names = ['team_id', 'team_name', 'player_id', 'player_name']

            mask = (player_stats.index.get_level_values('team_id') == team) & \
                (player_stats.index.get_level_values('player_name') == goalkeeper)
            
            # Check if there are any matching rows
            if mask.any():
                for stat in ['total_saves', 'successful_saves', 'save_rate']:
                    print(team_stats.columns)
                    if stat in team_stats.columns:
                        # Update stats for matching rows
                        player_stats.loc[mask, stat] = team_stats.loc[team, stat]


    
    for col in player_stats.columns:
        if col != 'pass_accuracy':
            player_stats[col] = player_stats[col].fillna(0).astype(int)

    # print("player_stats columns:", player_stats)
    # print("playing_times columns:", playing_times)

    player_stats.reset_index(inplace=True)
    player_stats.rename(columns={"level_0": "team_id", "level_1": "team_name", "level_2": "player_id", "level_3": "player_name"}, inplace=True)

    player_stats = pd.merge(player_stats, playing_times, left_on='player_id', right_on='player_id')

    cols = player_stats.columns.tolist()
    cols = cols[:4] + ['playing_time'] + cols[4:-2]

    print(player_stats.columns)

    return player_stats.to_dict(orient='records')

# 대회 선수들 통계 합산 반환 -> TOP 10까지 반환 및 특정 선수 통계 반환
@router.post("/group")
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
@router.get("/sequence/{current_time}")
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
@router.get("/shots/{current_time}")
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
@router.get("/setpieces/{current_time}")
def get_setpieces(current_time: int):
    # Filter the data by time
    match_events = filter_by_time(match_events, end_time=current_time)

    # Filter out the set-piece situations
    set_piece_events = match_events[match_events['sub_event_type'].isin(['Corner', 'Free Kick'])]

    # Sort the events in chronological order
    set_piece_events_sorted = set_piece_events.sort_values(['period', 'time'])
    return set_piece_events_sorted.to_dict(orient='records')