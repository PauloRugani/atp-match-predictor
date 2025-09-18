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