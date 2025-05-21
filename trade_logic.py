import datetime
import pandas as pd
from upstox_utils import place_order, get_positions

TRADE_LOG = "trade_log.csv"

def log_trade(timestamp, symbol, action, qty, price):
    new_trade = pd.DataFrame([[timestamp, symbol, action, qty, price]],
                             columns=['timestamp', 'symbol', 'action', 'qty', 'price'])
    new_trade.to_csv(TRADE_LOG, mode='a', index=False, header=not pd.io.common.file_exists(TRADE_LOG))

def execute_straddle(symbol, strike_price, qty):
    timestamp = datetime.datetime.now()
    ce_symbol = f"{symbol}{strike_price}CE"
    pe_symbol = f"{symbol}{strike_price}PE"

    ce_order = place_order(ce_symbol, 'sell', qty)
    pe_order = place_order(pe_symbol, 'sell', qty)

    log_trade(timestamp, ce_symbol, 'sell', qty, 'market')
    log_trade(timestamp, pe_symbol, 'sell', qty, 'market')

    return ce_order, pe_order

def close_all_positions():
    positions = get_positions()
    timestamp = datetime.datetime.now()

    for pos in positions:
        if pos['net_quantity'] != 0:
            action = 'buy' if pos['net_quantity'] < 0 else 'sell'
            place_order(pos['symbol'], action, abs(pos['net_quantity']))
            log_trade(timestamp, pos['symbol'], action, abs(pos['net_quantity']), 'market')
