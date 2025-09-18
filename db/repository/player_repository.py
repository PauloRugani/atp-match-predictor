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

def clear_table(table_name: str):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM {table_name}")
    conn.commit()
    conn.close()