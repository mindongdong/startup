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
        frameNum = currentFrameNum.frame - 20
    return list(predictions[str(i)][frameNum] for i in range(6))
    # return [predictions[str(0)][frameNum], 
    # predictions[str(1)][frameNum],
    # predictions[str(2)][frameNum],
    # predictions[str(3)][frameNum],
    # predictions[str(4)][frameNum],]

# print(type(trackingBtn(0)))