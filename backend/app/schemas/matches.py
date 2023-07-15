from typing import Optional
from typing import Optional
from pydantic import BaseModel

class Events(BaseModel):
    player_name: Optional[str] = None
    event_type: Optional[str] = None 
    sub_event_type: Optional[str] = None 
    team_name: Optional[str] = None 
    tags: Optional[str] = None 
    start_time: Optional[int] = None 
    end_time: Optional[int] = None

class Player(BaseModel):
    player_name: Optional[str] = None
    stats: Optional[str] = None