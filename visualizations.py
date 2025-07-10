from load_data import load_event_data
from basic_metrics import calculate_dau
import matplotlib.pyplot as plt

def plot_dau(df):
    dau = calculate_dau(df)
    plt.figure(figsize=(10, 5))
    dau.plot(marker='o')
    plt.title("Daily Active Users")
    plt.ylabel("Unique Users")
    plt.xlabel("Date")
    plt.grid()
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    df = load_event_data()
    plot_dau(df)