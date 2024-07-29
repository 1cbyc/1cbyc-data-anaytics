import pandas as pd

def calculate_summary_statistics(df):
    return df.describe()

def calculate_correlation(df):
    return df.corr()
