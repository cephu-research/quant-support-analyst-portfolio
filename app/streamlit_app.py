import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="Market Regime Dashboard", layout="wide")
st.title("Market Regime Dashboard")

st.markdown("A lightweight dashboard prototype for a trading or investment team. Data from Yahoo Finance via yfinance.")

tickers = st.multiselect("Tickers", ["SPY", "QQQ", "IWM", "TLT", "GLD", "UUP", "^VIX"], default=["SPY", "QQQ", "^VIX"])
start = st.date_input("Start date", pd.to_datetime("2020-01-01"))

if tickers:
    data = yf.download(tickers, start=start, auto_adjust=True, progress=False)
    prices = data["Close"] if isinstance(data.columns, pd.MultiIndex) else data[["Close"]]
    st.subheader("Adjusted close prices")
    st.plotly_chart(px.line(prices, title="Price history"), use_container_width=True)

    returns = prices.pct_change()
    vol = returns.rolling(21).std() * np.sqrt(252)
    st.subheader("21-day annualized volatility")
    st.plotly_chart(px.line(vol, title="Rolling volatility"), use_container_width=True)
