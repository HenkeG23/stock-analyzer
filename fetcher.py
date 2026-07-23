
import yfinance as yf
import streamlit as st

@st.cache_data(ttl=300)
def get_stock_data(ticker: str):
    stock = yf.Ticker(ticker)
    info = stock.info
    
    if not info or info.get("regularMarketPrice") is None:
        raise ValueError (f"No data found for ticker '{ticker}'. ")

    return info

from ratios import get_key_ratios

@st.cache_data(ttl=300)
def get_price_history(ticker: str, period: str = "6mo"):
    stock = yf.Ticker(ticker)
    history = stock.history(period)

    if history.empty:
        raise ValueError(f"No historic data for ticker '{ticker}'.")
    
    return history
@st.cache_data(ttl=300)
def get_put_call_ratio(ticker: str):
    stock = yf.Ticker(ticker)
    expirations = stock.options

    if not expirations:
        raise ValueError(f"No data available for '{ticker}'.")

    per_expiration = {}
    total_put_volume = 0
    total_call_volume = 0

    for date in expirations:
        chain = stock.option_chain(date)
        put_volume = chain.puts["volume"].sum()
        call_volume = chain.calls["volume"].sum()

        total_put_volume += put_volume
        total_call_volume += call_volume

        if call_volume > 0:
            per_expiration[date] = round(float(put_volume) / float(call_volume), 2)
        else:
            per_expiration[date] = None

    if total_call_volume > 0:
        total_ratio = round(float(total_put_volume) / float(total_call_volume), 2)
    else:
        total_ratio = None

    return {
        "per_expiration": per_expiration,
        "total": total_ratio,
    }


if __name__ == "__main__":
       
    ticker = input("Ticker: ")
    try:
        data = get_stock_data(ticker)
        ratios = get_key_ratios(data)
        for name, value in ratios.items():
            print(f"{name}: {value}")
    except ValueError as e:
        print(e)


