from load_data import load_event_data
import pandas as pd

def calculate_dau(df):
    dau = df.groupby(df['timestamp'].dt.date)['user_id'].nunique()
    return dau

if __name__ == '__main__':
    df = load_event_data()
    dau = calculate_dau(df)
    print("DAU:\n", dau)