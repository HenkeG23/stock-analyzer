# Stock Analyzer

A Streamlit web app for analyzing stocks with a focus on risk-adjusted metrics.

## Features

- Key financial ratios across four categories: Valuation, Profitability, Risk & Debt, and Other
- Interactive price history chart with selectable time period
- Put/Call ratio breakdown by option expiration date, plus a total ratio
- Risk-adjusted metrics: Sharpe Ratio, Sortino Ratio, and Maximum Drawdown, with adjustable time period and risk-free rate
- Supports both US and European tickers (e.g. `AAPL`, `VOLV-B.ST`)

<!-- ![App screenshot](screenshot.png) -->


## Tech Stack

- Python
- Streamlit (UI)
- yfinance (data source)
- pandas / NumPy (calculations)

## Running Locally

1. Clone the repo:
```bash
   git clone https://github.com/HenkeG23/stock-analyzer.git
   cd stock-analyzer
```

2. Create and activate a virtual environment:
```bash
   python -m venv venv
   venv\Scripts\activate
```

3. Install dependencies:
```bash
   pip install -r requirements.txt
```

4. Run the app:
```bash
   streamlit run app.py
```

## Project Background

Built as a portfolio project to explore risk-adjusted stock analysis, going beyond standard valuation metrics to include volatility- and drawdown-based measures.