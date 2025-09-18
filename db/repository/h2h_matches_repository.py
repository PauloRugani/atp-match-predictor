from models.MatchH2H import MatchH2H
from models.MatchH2H import MatchH2H
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

