from models.PlayerStats import PlayerStats
import sqlite3
from dotenv import load_dotenv
import os

load_dotenv()
DB_PATH = os.getenv('DB_PATH')

def insert_player_stats(stats: PlayerStats):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT OR REPLACE INTO player_stats (
            PLAYER_ID, CLAY_RATING, RATING, GRASS_RATING, HARD_RATING,
            CARPET_RATING, PERC_WIN_LAST_10, PERC_WIN_LAST_25,
            PERC_WIN_LAST_50, PERC_WIN_LAST_100, PERC_WIN_COMBINED
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        stats.PLAYER_ID,
        stats.CLAY_RATING,
        stats.RATING,
        stats.GRASS_RATING,
        stats.HARD_RATING,
        stats.CARPET_RATING,
        stats.PERC_WIN_LAST_10,
        stats.PERC_WIN_LAST_25,
        stats.PERC_WIN_LAST_50,
        stats.PERC_WIN_LAST_100,
        stats.PERC_WIN_COMBINED
    ))
    conn.commit()
    conn.close()


def clear_table(table_name: str):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM {table_name}")
    conn.commit()
    conn.close()