import streamlit as st
from fetcher import get_stock_data, get_price_history
from ratios import get_key_ratios
from formatters import format_large_numbers

st.title("Stock Analyzer")

ticker = st.text_input("Ticker Symbol", value="AAPL")

if st.button("Analyze"):
    st.session_state.ticker = ticker

if "ticker" in st.session_state:
    try:
        data = get_stock_data(st.session_state.ticker)
        ratios = get_key_ratios(data)

        st.subheader(f"Key metrics for {st.session_state.ticker}")

        tabs = st.tabs(list(ratios.keys()))

        for tab, (category, metrics) in zip(tabs, ratios.items()):
            with tab:
                cols = st.columns(3)
                for i, (name, value) in enumerate(metrics.items()):
                    if name in ["Market cap", "Free cash flow"]:
                        display_value = format_large_numbers(value)
                    elif name == "Dividend Yield":
                        display_value = f"{value}%"
                    elif isinstance(value, float):
                        display_value = round(value, 2)
                    else:
                        display_value = value
                    
                    cols[i % 3].metric(label=name, value=display_value)

        st.subheader("Price Development")

        period_options = {
            "1 Month": "1mo",
        "6 Months": "6mo",
        "1 Year": "1y",
        "5 Years": "5y",
        "Max": "max",
        }

        selected_label = st.selectbox("Select Time Period", list(period_options.keys()), index=1)
        selected_period = period_options[selected_label]
        

        history = get_price_history(st.session_state.ticker, period=selected_period)
        st.line_chart(history["Close"])

    except ValueError as e:
        st.error(str(e))