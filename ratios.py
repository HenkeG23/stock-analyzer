

def get_key_ratios(data: dict) -> dict:
    return {
        "Valuation": {
            "Market cap": data.get("marketCap"),
            "Currency": data.get("currency"),
            "Current Price": data.get("currentPrice"),
            "P/E (trailing)": data.get("trailingPE"),
            "P/E (forward)": data.get("forwardPE"),
            "PEG": data.get("pegRatio"),
            "P/B": data.get("priceToBook"),
        },
        "Profitability": {
            "EPS": data.get("epsCurrentYear"),
            "Forward EPS": data.get("epsForward"),
            "Earnings Growth": data.get("earningsGrowth"),
            "ROE": data.get("returnOnEquity"),
            "ROA": data.get("returnOnAssets"),
            "Profit margins": data.get("profitMargins"),
        },
        "Risk & Debt": {
            "debtToEquity": data.get("debtToEquity"),
            "Current Ratio": data.get("currentRatio"),
            "beta": data.get("beta"),
            "52 weeks change": data.get("52WeekChange"),
            "Free cash flow": data.get("freeCashflow"),
        },
        "Other": {
            "Dividend Yield": data.get("dividendYield"),
            "Sector": data.get("sector"),
            "Country": data.get("country"),
            "200 days average": data.get("twoHundredDayAverage"),
            "Recommendation": data.get("recommendationKey"),
            "Recommendation Score": data.get("recommendationMean"),
            "Target Mean": data.get("targetMeanPrice"),
        },
    }