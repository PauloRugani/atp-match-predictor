from pydantic import BaseModel
from typing import Optional

class PlayerStats(BaseModel):
    PLAYER_ID: str
    RATING: float 
    CLAY_RATING: Optional[float] = 2000
    GRASS_RATING: Optional[float] = 2000
    HARD_RATING: Optional[float] = 2000
    CARPET_RATING: Optional[float] = 2000
    PERC_WIN_LAST_10: float
    PERC_WIN_LAST_25: float
    PERC_WIN_LAST_50: float
    PERC_WIN_LAST_100: float
    PERC_WIN_COMBINED: float

