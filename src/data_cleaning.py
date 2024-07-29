import pandas as pd

def clean_data(df):
    df = df.dropna()
    df = df.drop_duplicates()
    return df

def load_data(file_path):
    return pd.read_csv(file_path)
