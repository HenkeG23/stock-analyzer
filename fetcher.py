
import yfinance as yf

def get_stock_data(ticker: str):
    stock = yf.Ticker(ticker)
    info = stock.info
    
    if not info or info.get("regularMarketPrice") is None:
        raise ValueError (f"No data found for ticker '{ticker}'. ")

    return info

from ratios import get_key_ratios

def get_price_history(ticker: str, period: str = "6mo"):
    stock = yf.Ticker(ticker)
    history = stock.history(period)

    if history.empty:
        raise ValueError(f"No historic data for ticker '{ticker}'.")
    
    return history


if __name__ == "__main__":
       
    ticker = input("Ticker: ")
    try:
        data = get_stock_data(ticker)
        ratios = get_key_ratios(data)
        for name, value in ratios.items():
            print(f"{name}: {value}")
    except ValueError as e:
        print(e)

    