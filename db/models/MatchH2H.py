from pydantic import BaseModel

class MatchH2H(BaseModel):
    PLAYER1_ID: str
    PLAYER2_ID: str
    PLAYER1_WINS: int
    PLAYER2_WINS: int