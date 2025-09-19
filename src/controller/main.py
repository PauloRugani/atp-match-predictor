from joblib import load
from typing import Any, Literal, Tuple
from database.repository.player_repository import get_player_by_name
from database.repository.player_stats_repository import get_player_stats_by_name
from database.repository.h2h_matches_repository import get_h2h_match
import datetime

def parse_age(birthdate: datetime.date) -> int:
    today = datetime.date.today()
    year, month, day =  today.year, today.month, today.day

    age = year - birthdate.year - ((month, day) < (birthdate.month, birthdate.day))
    return age

def predict_winner(player0_name, player1_name, best_of: int, surface: str) -> int | str:
    try:
        player0_names = (player0_name.split(' ')[:1][0], ' '.join(player0_name.split(' ')[1:]))
        player1_names = (player1_name.split(' ')[:1][0], ' '.join(player1_name.split(' ')[1:]))

        player0_info = get_player_by_name(*player0_names)
        player1_info = get_player_by_name(*player1_names)
        
        player0_stats = get_player_stats_by_name(*player0_names)
        player1_stats = get_player_stats_by_name(*player1_names)

        player_0_id = player0_info.PLAYER_ID
        player_1_id = player1_info.PLAYER_ID

        list_players = sorted([player_0_id, player_1_id])
        h2h_match = get_h2h_match(list_players[0], player_1_id[1])

        h2h = {f'{list_players[0]}': h2h_match.PLAYER1_WINS,
               f'{list_players[1]}': h2h_match.PLAYER2_WINS}
        
        AGE_DIFF = round(parse_age(player0_info.BIRTHDATE) - parse_age(player1_info.BIRTHDATE), 2)
        HT_DIFF = round(player0_info.HEIGHT - player1_info.HEIGHT, 2)

        WINS_VS_1, WINS_VS_0 = h2h[player_0_id], h2h[player_1_id]
        TOTAL_MATCHES = WINS_VS_1 + WINS_VS_0
        WIN_RATE_0 = round((WINS_VS_1 / TOTAL_MATCHES), 2) if TOTAL_MATCHES > 0 else 0 
        WIN_RATE_1 = round((WINS_VS_0 / TOTAL_MATCHES), 2) if TOTAL_MATCHES > 0 else 0
        WIN_RATE_DIFF = WIN_RATE_0 - WIN_RATE_1

        RATING_DIFF = round(player0_stats.RATING - player1_stats.RATING, 2)
        SURFACE_RATING_DIFF = round(getattr(player0_stats, f'{surface.upper()}_RATING') - getattr(player1_stats, f'{surface.upper()}_RATING'), 2)
        LAST_10_WIN_DIFF = round(player0_stats.PERC_WIN_LAST_10 - player1_stats.PERC_WIN_LAST_25, 2)
        LAST_25_WIN_DIFF = round(player0_stats.PERC_WIN_LAST_25 - player1_stats.PERC_WIN_LAST_25, 2)
        LAST_50_WIN_DIFF = round(player0_stats.PERC_WIN_LAST_50 - player1_stats.PERC_WIN_LAST_50, 2)
        LAST_100_WIN_DIFF = round(player0_stats.PERC_WIN_LAST_100 - player1_stats.PERC_WIN_LAST_100, 2)
        WIN_COMBINED_DIFF = round(player0_stats.PERC_WIN_COMBINED - player1_stats.PERC_WIN_COMBINED, 2)

        data = [[
            best_of, AGE_DIFF, HT_DIFF, WINS_VS_1, WINS_VS_0, TOTAL_MATCHES, WIN_RATE_0, WIN_RATE_1, WIN_RATE_DIFF, 
            player0_stats.RATING, player1_stats.RATING, RATING_DIFF, getattr(player0_stats, f'{surface.upper()}_RATING'),
            getattr(player1_stats, f'{surface.upper()}_RATING'), SURFACE_RATING_DIFF, player0_stats.PERC_WIN_LAST_10, 
            player0_stats.PERC_WIN_LAST_25, player0_stats.PERC_WIN_LAST_50, player0_stats.PERC_WIN_LAST_100, 
            player0_stats.PERC_WIN_COMBINED, player1_stats.PERC_WIN_LAST_10, player1_stats.PERC_WIN_LAST_25, 
            player1_stats.PERC_WIN_LAST_50, player1_stats.PERC_WIN_LAST_100, player1_stats.PERC_WIN_COMBINED, 
            LAST_10_WIN_DIFF, LAST_25_WIN_DIFF, LAST_50_WIN_DIFF, LAST_100_WIN_DIFF, WIN_COMBINED_DIFF
        ]]

        model = load(r'model\xgboost_model.joblib')
        predict = model.predict(data)[0]
        return predict
    except Exception:
        return 'Sem informações suficientes para prever o resultado'
    
