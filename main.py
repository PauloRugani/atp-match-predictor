import pandas as pd
from src.controller.main import predict_winner
from typing import List, Tuple
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, accuracy_score
import csv

def run() -> Tuple[List[dict], float]:
    ao_open_matches = pd.read_csv(r'data\external\australia_open_matches.csv', sep=',', encoding='utf-8')
    correct_result = ao_open_matches['winner']
    print(ao_open_matches['winner'].value_counts())
    results = []
    model_result = []
    for _, row in ao_open_matches.iterrows():
        result = predict_winner(row['player_0'], row['player_1'], 5, 'HARD')

        if result == 0:
            winner = row['player_0']
            model_result.append(0)
        elif result == 1:
            winner = row['player_1']
            model_result.append(1)
        else:
            winner = 'Informações insuficientes para prever o resultado.'
            model_result.append(1)

        results.append({
            'player_0': row['player_0'],
            'player_1': row['player_1'],
            'predicted_winner': winner,
            'real_winner': row[f'player_{row["winner"]}'] 
        })
    return results, correct_result, model_result

ao_predict_result, correct_result, model_result = run()

accuracy = accuracy_score(correct_result, model_result)
print(f'Accuracy: {round((accuracy * 100), 2)}%')

plt.figure()
matrix = confusion_matrix(correct_result, model_result)
sns.heatmap(matrix, annot=True, fmt='d')
plt.show()

with open('./data/external/australia_open_predict.csv', mode='w', encoding='utf-8', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['player_0', 'player_1', 'predicted_winner', 'real_winner'])
    writer.writeheader()
    writer.writerows(ao_predict_result)
