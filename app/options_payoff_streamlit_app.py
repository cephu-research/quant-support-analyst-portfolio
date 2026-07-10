import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Options Payoff Analyzer", layout="wide")
st.title("Options Payoff Analyzer")
st.markdown("Prototype tool for visualizing simple option strategies. Educational use only.")

spot = st.number_input("Current underlying price", value=500.0)
low = st.number_input("Chart min price", value=400.0)
high = st.number_input("Chart max price", value=600.0)

strategy = st.selectbox("Example strategy", ["Bull Put Spread", "Iron Condor", "1-2-1 Put Fly"])
prices = np.linspace(low, high, 301)

def put_payoff(S, K, premium, qty):
    return qty * (np.maximum(K - S, 0) - premium)

def call_payoff(S, K, premium, qty):
    return qty * (np.maximum(S - K, 0) - premium)

if strategy == "Bull Put Spread":
    payoff = put_payoff(prices, spot*0.98, 4.0, -1) + put_payoff(prices, spot*0.95, 2.0, 1)
elif strategy == "Iron Condor":
    payoff = put_payoff(prices, spot*0.95, 3.0, -1) + put_payoff(prices, spot*0.90, 1.5, 1) + call_payoff(prices, spot*1.05, 3.0, -1) + call_payoff(prices, spot*1.10, 1.5, 1)
else:
    payoff = put_payoff(prices, spot*0.98, 1.0, 1) + put_payoff(prices, spot*0.95, 2.0, -2) + put_payoff(prices, spot*0.92, 1.0, 1)

chart = pd.DataFrame({"underlying_price": prices, "payoff": payoff})
st.plotly_chart(px.line(chart, x="underlying_price", y="payoff", title=strategy), use_container_width=True)
st.write(chart.describe())
