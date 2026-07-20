
def get_key_ratios(data: dict) -> dict:
    return {
        "Market cap": data.get("marketCap"),
        "P/E (trailing)": data.get("trailingPE"),
        "P/E (forward)": data.get("forwardPE"),
        "PEG": data.get("pegRatio"),
        "Sector": data.get("sector"),
        "200 days average": data.get("twoHundredDayAverage")

    }