import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


def load_data(path):
    # Read the data from the csv file
    df = pd.read_csv(path)
    return df
    

def process_stats(df):
    print("Columns available to us: ", df.columns.tolist())
    return df

def train_and_predict(features, targets):
    pass

def plot_likelihood(results):
    pass



if __name__ == "__main__":
    print("Model Training Intialized...")
    path = r"C:\Users\svyat\Downloads\E0 (1).csv"
    df = load_data(path)

    process_stats(df)

