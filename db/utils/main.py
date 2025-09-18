import sqlite3
from dotenv import load_dotenv
import os

load_dotenv()
DB_PATH = os.getenv('DB_PATH')

def clear_table(table_name: str):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM {table_name}")
    conn.commit()
    conn.close()