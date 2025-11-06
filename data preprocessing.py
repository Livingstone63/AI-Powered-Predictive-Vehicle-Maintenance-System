import pandas as pd

def preprocess_data(df):
    """Cleans and validates input data."""
    df = df.dropna()
    df = df[df["engine_temp"] > 0]
    return df
