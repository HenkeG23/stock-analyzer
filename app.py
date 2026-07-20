import streamlit as st
from fetcher import get_stock_data
from ratios import get_key_ratios

st.title("Stock Analyzer")

ticker = st.text_input("Name Ticker", value ="AAPL")

if st.button("Analyz"):
    try:
        data = get_stock_data(ticker)
        ratios = get_key_ratios(data)

        st.subheader(f"Key metrics for {ticker}")
        for name, value in ratios.items():
            st.markdown(f"**{name}: **{value}")
    
    except ValueError as e:
        st.error(str(e))

