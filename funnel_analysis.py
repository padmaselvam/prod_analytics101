from load_data import load_event_data
import pandas as pd

def funnel(df, steps):
    funnel_counts = {}
    for i, step in enumerate(steps):
        if i == 0:
            users = df[df['event_name'] == step]['user_id'].unique()
        else:
            users = df[df['event_name'] == step]
            users = users[users['user_id'].isin(funnel_counts[steps[i-1]])]['user_id'].unique()
        funnel_counts[step] = users
    return {step: len(users) for step, users in funnel_counts.items()}

if __name__ == '__main__':
    df = load_event_data()
    steps = ['signup', 'login', 'purchase']
    funnel_result = funnel(df, steps)
    print("Funnel Analysis:", funnel_result)