import pandas as pd

def load_event_data(path='data/sample_events.csv'):
    df = pd.read_csv(path, parse_dates=['timestamp'])
    return df

if __name__ == '__main__':
    df = load_event_data()
    print(df.head())