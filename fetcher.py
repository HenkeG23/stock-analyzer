
import yfinance as yf

def get_stock_data(ticker: str):
    stock = yf.Ticker(ticker)
    info = stock.info
    return info

from ratios import get_key_ratios

if __name__ == "__main__":
    data = get_stock_data("AAPL")
    ratios = get_key_ratios(data)
    for name, value in ratios.items():
        print(f"{name}: {value}")
        

    