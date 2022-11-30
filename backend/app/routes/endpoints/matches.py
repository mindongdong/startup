from fastapi import APIRouter
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel
import pandas as pd
import os
import json

router = APIRouter()

class matchInfo(BaseModel):
    match_name: str

@router.post("/info")
def checkInfo(match_info: matchInfo):
    teams = match_info.match_name.split('.')
    team1 = teams[0]
    team2 = teams[1]
    print(team1, team2)
    PATH_MATCH_INFO = f'./matches/{match_info.match_name}/'
    match_list = os.listdir(PATH_MATCH_INFO)
    match_data = []
    print(PATH_MATCH_INFO + match_list[0])
    for data in match_list:
        print(data)
        with open(PATH_MATCH_INFO + data, 'r') as file:
            file_data = pd.read_csv(file).fillna('').to_dict().copy()
            print(file_data)
            match_data.append(file_data) 

    return JSONResponse(match_data)