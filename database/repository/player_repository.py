from models.Player import Player
import sqlite3
from dotenv import load_dotenv
import os

load_dotenv()
DB_PATH = os.getenv('DB_PATH')

def insert_player(player: Player):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT OR REPLACE INTO players (
            PLAYER_ID, FIRST_NAME, LAST_NAME, HAND, BIRTHDATE, COUNTRY, HEIGHT
        ) VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        player.PLAYER_ID,
        player.FIRST_NAME,
        player.LAST_NAME,
        player.HAND,
        player.BIRTHDATE,
        player.COUNTRY,
        player.HEIGHT
    ))
    conn.commit()
    conn.close()

def get_player_by_name(first_name: str, last_name: str) -> Player | None:
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT PLAYER_ID, HAND, BIRTHDATE, COUNTRY, HEIGHT
        FROM players
        WHERE FIRST_NAME = ? AND LAST_NAME = ?
    """, (
        first_name, last_name
    ))
    row = cursor.fetchone()
    conn.close()
    if row:
        return Player(
            PLAYER_ID=row[0],
            FIRST_NAME=first_name,
            LAST_NAME=last_name,
            HAND=row[1],
            BIRTHDATE=row[2],
            COUNTRY=row[3],
            HEIGHT=row[4] 
        )
    return None
