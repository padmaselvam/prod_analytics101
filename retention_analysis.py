from load_data import load_event_data
import pandas as pd

def retention_matrix(df):
    df['signup_date'] = df[df['event_name'] == 'signup'].groupby('user_id')['timestamp'].transform('min')
    df = df[df['event_name'] == 'login']
    df['days_since_signup'] = (df['timestamp'] - df['signup_date']).dt.days
    cohort = df.groupby(['signup_date', 'days_since_signup'])['user_id'].nunique().unstack().fillna(0)
    return cohort

if __name__ == '__main__':
    df = load_event_data()
    cohort = retention_matrix(df)
    print("Retention Cohort:\n", cohort)