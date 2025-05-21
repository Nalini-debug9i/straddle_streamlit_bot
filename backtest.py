import pandas as pd

def run_backtest(df):
    df['pnl'] = df.apply(lambda row: row['qty'] * (-10 if row['action'] == 'sell' else 10), axis=1)  # example logic
    total_pnl = df['pnl'].sum()
    daily = df.copy()
    daily['date'] = pd.to_datetime(daily['timestamp']).dt.date
    daily_pnl = daily.groupby('date')['pnl'].sum()
    return total_pnl, daily_pnl
