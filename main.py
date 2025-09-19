import pandas as pd
from src.controller.main import predict_winner
from typing import List, Tuple
import csv

def run() -> Tuple[List[dict], float]:
    ao_open_matches = pd.read_csv(r'data\external\australia_open_matches.csv', sep=',', encoding='utf-8')
    results = []
    correct = 0
    for _, row in ao_open_matches.iterrows():
        result = predict_winner(row['player_0'], row['player_1'], 5, 'HARD')

        if result == 0:
            winner = row['player_0']
            correct += 1
        elif result == 1:
            winner = row['player_1']
        else:
            winner = 'Informações insuficientes para prever o resultado.'

        results.append({
            'player_0': row['player_0'],
            'player_1': row['player_1'],
            'predicted_winner': winner,
            'real_winner': row['player_0'] # player_0 is the winner
        })
    accuracy = round((correct / len(ao_open_matches)), 2)
    return results, accuracy

ao_predict_result, accuracy = run()
print(f'Accuracy: {accuracy * 100}%')

with open('./data/external/australia_open_predict.csv', mode='w', encoding='utf-8', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['player_0', 'player_1', 'predicted_winner', 'real_winner'])
    writer.writeheader()
    writer.writerows(ao_predict_result)
