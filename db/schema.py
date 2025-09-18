import sqlite3
from dotenv import load_dotenv
import os

load_dotenv()
DB_PATH = os.getenv('DB_PATH')

def create_tables():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.executescript("""
    CREATE TABLE IF NOT EXISTS players (
        PLAYER_ID TEXT PRIMARY KEY,
        FIRST_NAME TEXT NOT NULL,
        LAST_NAME TEXT NOT NULL,
        HAND TEXT,
        BIRTHDATE DATE,
        COUNTRY TEXT,
        HEIGHT REAL
    );

    CREATE TABLE IF NOT EXISTS player_stats (
        PLAYER_ID TEXT PRIMARY KEY,
        CLAY_RATING REAL,
        RATING REAL,
        GRASS_RATING REAL,
        HARD_RATING REAL,
        CARPET_RATING REAL,
        PERC_WIN_LAST_10 REAL,
        PERC_WIN_LAST_25 REAL,
        PERC_WIN_LAST_50 REAL,
        PERC_WIN_LAST_100 REAL,
        PERC_WIN_COMBINED REAL,
        FOREIGN KEY (PLAYER_ID) REFERENCES players(PLAYER_ID)
    );

    CREATE TABLE IF NOT EXISTS matches_h2h (
        PLAYER1_ID TEXT,
        PLAYER2_ID TEXT,
        PLAYER1_WINS INTEGER,
        PLAYER2_WINS INTEGER,
        PRIMARY KEY (PLAYER1_ID, PLAYER2_ID),
        FOREIGN KEY (PLAYER1_ID) REFERENCES players(PLAYER_ID),
        FOREIGN KEY (PLAYER2_ID) REFERENCES players(PLAYER_ID)
    );
    """)

    conn.commit()
    conn.close()