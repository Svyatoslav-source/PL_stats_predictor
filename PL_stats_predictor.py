import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt


def load_data(path):
    # Read the data from the csv file
    df = pd.read_csv(path)
    df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
    return df.sort_values('Date')
    

def get_rolling_stats(df, n_games=5):
    # Standardize data to track every team's history
    h = df[['Date', 'HomeTeam', 'FTHG', 'FTAG', 'FTR', 'HST']].copy()
    a = df[['Date', 'AwayTeam', 'FTAG', 'FTHG', 'FTR', 'AST']].copy()

    cols = ['Date', 'Team', 'GoalsFor', 'GoalsAgainst', 'Result', 'SOT']
    h.columns, a.columns = cols, cols

    # Calculate points for each game 
    def pts(res, is_home):
        if res == 'D': return 1
        if (res == 'H' and is_home) or (res=='A' and not is_home): return 3
        return 0
    
    h['Points'] = h['Result'].apply(lambda x: pts(x, True))
    a['Points'] = a['Result'].apply(lambda x: pts(x, False))

    all_games = pd.concat([h, a]).sort_values(['Team', 'Date'])
            

    # Calculate Rolling averages (The .shift(1) is used to prevent data leakage)
    for col in ['GoalsFor', 'GoalsAgainst', 'Points', 'SOT']:
        all_games[f'Rolling_{col}'] = all_games.groupby('Team')[col].transform(lambda x: x.rolling(n_games, closed='left').mean())
        return all_games    
    



if __name__ == "__main__":
    print("Model Training Intialized...")
    path = r"C:\Users\svyat\Downloads\E0 (1).csv"
    

