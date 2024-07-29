import pandas as pd

def clean_data(df):
    df = df.dropna()
    df = df.drop_duplicates()
    return df
def load_data(file_path):
    # return pd.read_csv(file_path)
    # updating the load_data to include error handling for empty files too
    try:
        df =pd.read_csv(file_path)
        if df.empty:
            raise ValueError("egbon your csv file is empty")
        return df
    except pd.errors.EmptyDataError:
        print(f"Nno data: the file at {file_path} dey empty or no contain any columns.")
        return pd.DataFrame()

def clean_data(df):
    df = df.dropna()
    df = df.drop_duplicates()
    return df


