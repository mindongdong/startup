import os
import json
from pydantic import BaseModel
from fastapi import APIRouter
from fastapi.responses import FileResponse, JSONResponse

router = APIRouter()

@router.get("/info/{frame}")
def trackingBtn(frame: int):
    # with open("/Users/seancho/VSCodeProjects/startup/backend/matches/predictions.json", 'r') as file:
    with open("./matches/predictions.json", 'r') as file:
        predictions = json.load(file)
        frameNum = int(frame*25/27) + 5
    return list(predictions[str(i)][frameNum] for i in range(23))
# print(type(trackingBtn(0)))