from models.MatchH2H import MatchH2H
import sqlite3
from dotenv import load_dotenv
import os

load_dotenv()
DB_PATH = os.getenv('DB_PATH')

def insert_h2h_match(h2h: MatchH2H):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT OR REPLACE INTO matches_h2h (
            PLAYER1_ID, PLAYER2_ID, PLAYER1_WINS, PLAYER2_WINS
        ) VALUES (?, ?, ?, ?)
    """, (
        h2h.PLAYER1_ID,
        h2h.PLAYER2_ID,
        h2h.PLAYER1_WINS,
        h2h.PLAYER2_WINS
    ))
    conn.commit()
    conn.close()

def get_h2h_match(player1_id: int, player2_id: int) -> MatchH2H | None:
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT PLAYER1_ID, PLAYER2_ID, PLAYER1_WINS, PLAYER2_WINS
        FROM matches_h2h
        WHERE (PLAYER1_ID = ? AND PLAYER2_ID = ?) OR (PLAYER1_ID = ? AND PLAYER2_ID = ?)
    """, (player1_id, player2_id, player2_id, player1_id))
    row = cursor.fetchone()
    conn.close()
    if row:
        return MatchH2H(
            PLAYER1_ID=row[0],
            PLAYER2_ID=row[1],
            PLAYER1_WINS=row[2],
            PLAYER2_WINS=row[3]
        )
    return None
