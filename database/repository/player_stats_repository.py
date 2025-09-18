from models.PlayerStats import PlayerStats
import sqlite3
from dotenv import load_dotenv
import os
from typing import Optional

load_dotenv()
DB_PATH = os.getenv('DB_PATH')

def insert_player_stats(stats: PlayerStats):
    with sqlite3.connect(DB_PATH) as conn:
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

def get_player_stats_by_name(first_name: str, last_name: str) -> Optional[PlayerStats]:
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT ps.PLAYER_ID, ps.CLAY_RATING, ps.RATING, ps.GRASS_RATING, ps.HARD_RATING,
                    ps.CARPET_RATING, ps.PERC_WIN_LAST_10, ps.PERC_WIN_LAST_25,
                    ps.PERC_WIN_LAST_50, ps.PERC_WIN_LAST_100, ps.PERC_WIN_COMBINED
            FROM player_stats ps
            INNER JOIN players p ON ps.PLAYER_ID = p.PLAYER_ID
            WHERE p.FIRST_NAME = ? and p.LAST_NAME= ? 
        """, (first_name, last_name))

        row = cursor.fetchone()
        print(row)
    if row:
        return PlayerStats(
            PLAYER_ID=row[0],
            CLAY_RATING=row[1],
            RATING=row[2],
            GRASS_RATING=row[3],
            HARD_RATING=row[4],
            CARPET_RATING=row[5],
            PERC_WIN_LAST_10=row[6],
            PERC_WIN_LAST_25=row[7],
            PERC_WIN_LAST_50=row[8],
            PERC_WIN_LAST_100=row[9],
            PERC_WIN_COMBINED=row[10]
        )
    return None
