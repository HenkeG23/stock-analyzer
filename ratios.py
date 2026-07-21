
def get_key_ratios(data: dict) -> dict:
    return {
        "Market cap": data.get("marketCap"),
        "Current Price": data.get("currentPrice"),
        "Currency": data.get("currency"),
        "Dividend Yield": data.get("dividendYield"),
        "P/E (trailing)": data.get("trailingPE"),
        "P/E (forward)": data.get("forwardPE"),
        "PEG": data.get("pegRatio"),
        "EPS": data.get("epsCurrentYear"),
        "Forward EPS": data.get("epsForward"),
        "Earnings Growth": data.get("earningsGrowth"),
        "Sector": data.get("sector"),
        "200 days average": data.get("twoHundredDayAverage"),
        "52 weeks change": data.get("52WeekChange"),
        "beta": data.get("beta"),
        "Country": data.get("country"),
        "Recommendations": data.get("recommendationKey"),
        "Recomendations Score": data.get("recommendationMean"),
        "Target Mean": data.get("targetMeanPrice"),
        "ROE": data.get("returnOnEquity"),
        "ROA": data.get("returnOnAssets"),
        "Profit margins": data.get("profitMargins"),
        "debtToEquity": data.get("debtToEquity"),
        "P/B": data.get("priceToBook"),
        "Free cash flow": data.get("freeCashflow"),
        "Current Ratio": data.get("currentRatio")

    }