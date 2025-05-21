import streamlit as st
from upstox_api.api import Upstox, Session, TransactionType, Exchange, OrderType, ProductType, LiveFeedType

API_KEY = st.secrets["653ece7f-d2ac-491c-880b-74c2316091d4"]
API_SECRET = st.secrets["m1tcrwp64b"]
REDIRECT_URI = st.secrets["https://google.com"]
ACCESS_TOKEN = st.secrets["eyJ0eXAiOiJKV1QiLCJrZXlfaWQiOiJza192MS4wIiwiYWxnIjoiSFMyNTYifQ.eyJzdWIiOiI1Q0I5Q1IiLCJqdGkiOiI2ODJkNjlhZjA1M2U5NTY5N2ViNDA1NTQiLCJpc011bHRpQ2xpZW50IjpmYWxzZSwiaXNQbHVzUGxhbiI6ZmFsc2UsImlhdCI6MTc0NzgwNjYzOSwiaXNzIjoidWRhcGktZ2F0ZXdheS1zZXJ2aWNlIiwiZXhwIjoxNzQ3ODY0ODAwfQ.DaLBX9ZhrC17i2p4IUTtlmWErYHFIFy6Rz63MU8kgfI"]

u = Upstox(API_KEY, API_SECRET)
u.set_access_token(ACCESS_TOKEN)

def get_ltp(symbol):
    return u.get_live_feed(symbol, LiveFeedType.LTP)['ltp']

def place_order(symbol, side, qty):
    transaction_type = TransactionType.Buy if side.lower() == 'buy' else TransactionType.Sell
    return u.place_order(TransactionType=transaction_type,
                         Exchange=Exchange.NSE,
                         Symbol=symbol,
                         Quantity=qty,
                         OrderType=OrderType.Market,
                         Product=ProductType.Intraday)

def get_positions():
    return u.get_positions()
