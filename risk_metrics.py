import numpy as np

def calculate_returns(price_history):
    return price_history["Close"].pct_change().dropna()


def calculate_sharpe_ratio(returns, risk_free_rate=0.02):
    excess_returns = returns - (risk_free_rate / 252)
    annualized_return = excess_returns.mean() * 252
    annualized_volatility = returns.std() * np.sqrt(252)
    
    if annualized_volatility == 0:
        return None
    
    return round(annualized_return / annualized_volatility, 2)


def calculate_sortino_ratio(returns, risk_free_rate=0.02):
    excess_returns = returns - (risk_free_rate / 252)
    annualized_return = excess_returns.mean() * 252
    
    downside_returns = returns[returns < 0]
    downside_deviation = downside_returns.std() * np.sqrt(252)
    
    if downside_deviation == 0 or np.isnan(downside_deviation):
        return None
    
    return round(annualized_return / downside_deviation, 2)


def calculate_max_drawdown(price_history):
    prices = price_history["Close"]
    running_max = prices.cummax()
    drawdown = (prices - running_max) / running_max
    
    return round(drawdown.min() * 100, 2)

if __name__ == "__main__":
    from fetcher import get_price_history
    history = get_price_history("AAPL", period="3y")
    returns = calculate_returns(history)
    
    print("Sharpe:", calculate_sharpe_ratio(returns))
    print("Sortino:", calculate_sortino_ratio(returns))
    print("Max Drawdown:", calculate_max_drawdown(history), "%")