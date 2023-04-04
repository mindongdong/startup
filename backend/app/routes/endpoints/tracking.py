import os
import json
from pydantic import BaseModel
from fastapi import APIRouter
from fastapi.responses import FileResponse, JSONResponse

router = APIRouter()

class currentFrameNum(BaseModel):
    frame: int

@router.post("/info")
def trackingBtn(currentFrameNum: currentFrameNum):
    PATH_MATCH_INFO = f'./matches/'
    # with open("/Users/seancho/VSCodeProjects/startup/backend/matches/predictions.json", 'r') as file:
    with open("./matches/predictions.json", 'r') as file:

        predictions = json.load(file)
    return predictions[str(currentFrameNum.frame)]['predictions']

# print(type(trackingBtn(0)))