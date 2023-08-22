import json
from fastapi import APIRouter

router = APIRouter()

with open("./matches/predictions.json", 'r') as file:
    predictions = json.load(file)

@router.get("/info/{frame}")
def trackingBtn(frame: int):
    # with open("/Users/seancho/VSCodeProjects/startup/backend/matches/predictions.json", 'r') as file:
    frameNum = frame
    return list(predictions[str(i)][frameNum] for i in range(23))
# print(type(trackingBtn(0)))