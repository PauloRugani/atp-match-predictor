from pydantic import BaseModel
from typing import Optional
from datetime import date

class Player(BaseModel):
    PLAYER_ID: str
    FIRST_NAME: str
    LAST_NAME: str
    HAND: Optional[str] = None
    BIRTHDATE: Optional[date] = None
    COUNTRY: Optional[str] = None
    HEIGHT: Optional[float] = None

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

class MatchH2H(BaseModel):
    PLAYER1_ID: str
    PLAYER2_ID: str
    PLAYER1_WINS: int
    PLAYER2_WINS: int