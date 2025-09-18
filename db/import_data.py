import csv
import json
from datetime import datetime
from models import Player, PlayerStats, MatchH2H
from repository import insert_player, insert_player_stats, insert_h2h_match
from schema import create_tables

def parse_date(val):
    if not val or val.strip() == "":
        return None
    try:
        return datetime.strptime(val, "%Y%m%d").date()
    except Exception:
        return None
    
def parse_float(val):
    try:
        return float(val)
    except (ValueError, TypeError):
        return None
    
def import_players(csv_path: str) -> None:
    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            player = Player(
                PLAYER_ID=row["player_id"],
                FIRST_NAME=row["name_first"],
                LAST_NAME=row["name_last"],
                HAND=row["hand"] or None,
                BIRTHDATE=parse_date(row["dob"]),
                COUNTRY=row["ioc"] or None,
                HEIGHT=parse_float(row["height"])
                )
            insert_player(player)

def import_player_stats_json(json_path: str) -> None:
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    for player_id, stats in data.items():
        stats_obj = PlayerStats(
            PLAYER_ID=player_id,
            RATING=stats.get("RATING"),
            CLAY_RATING=stats.get("CLAY_RATING"),
            GRASS_RATING=stats.get("GRASS_RATING"),
            HARD_RATING=stats.get("HARD_RATING"),
            CARPET_RATING=stats.get("CARPET_RATING"),
            PERC_WIN_LAST_10=stats.get("PERC_WIN_LAST_10"),
            PERC_WIN_LAST_25=stats.get("PERC_WIN_LAST_25"),
            PERC_WIN_LAST_50=stats.get("PERC_WIN_LAST_50"),
            PERC_WIN_LAST_100=stats.get("PERC_WIN_LAST_100"),
            PERC_WIN_COMBINED=stats.get("PERC_WIN_COMBINED")
        )
        insert_player_stats(stats_obj)

def import_h2h_matches(json_path: str) -> None:
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    for players, h2h_matches in data.items():
        player_0, player_1 = players.split('-')
        h2h_obj = MatchH2H(
            PLAYER1_ID=player_0,
            PLAYER2_ID=player_1,
            PLAYER1_WINS=h2h_matches.get(f"PLAYER_{player_0}_WINS"),
            PLAYER2_WINS=h2h_matches.get(f"PLAYER_{player_1}_WINS")
        )
        insert_h2h_match(h2h_obj)


if __name__ == "__main__":
    create_tables()
    import_players(r'data\raw\atp_players.csv')
    import_player_stats_json(r'data\players_ratings.json')
    import_h2h_matches(r'data\players_h2h.json')