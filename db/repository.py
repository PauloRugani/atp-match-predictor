from models import Player, PlayerStats, MatchH2H 
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

def insert_player_stats(stats: PlayerStats):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT OR REPLACE INTO player_stats (
            PLAYER_ID, CLAY_RATING, RATING, GRASS_RATING, HARD_RATING,
            CARPET_RATING, PERC_WIN_LAST_10, PERC_WIN_LAST_25,
            PERC_WIN_LAST_50, PERC_WIN_LAST_100
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
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
        stats.PERC_WIN_LAST_100
    ))
    conn.commit()
    conn.close()

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