
import yfinance as yf
import pandas as pd

def get_stock_data(ticker: str):
    stock = yf.Ticker(ticker)
    info = stock.info
    
    if not info or info.get("regularMarketPrice") is None:
        raise ValueError (f"No data found for ticker '{ticker}'. ")

    return info

from ratios import get_key_ratios

tabell = {
    "Exchange": ["Stockholm OMX", "Frankfurt"],
    "Suffix": [".ST", ".DE"],
    "Exempel": ["VOLV-B.ST", "SAP.DE"]
}

df = pd.DataFrame(tabell)

if __name__ == "__main__":
    print(df)    
    ticker = input("Ticker: ")
    try:
        data = get_stock_data(ticker)

        for key in sorted(data.keys()):
            print(key)

        ratios = get_key_ratios(data)
        for name, value in ratios.items():
            print(f"{name}: {value}")
    except ValueError as e:
        print(e)

    