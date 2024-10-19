# helpers.py
import pandas as pd
import os

def load_data(file_name, columns):
    if os.path.exists(file_name):
        return pd.read_csv(file_name)
    else:
        return pd.DataFrame(columns=columns)

def save_data(df, file_name):
    df.to_csv(file_name, index=False)
