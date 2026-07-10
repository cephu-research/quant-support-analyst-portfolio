import pandas as pd
import numpy as np
import yfinance as yf


def download_prices(tickers, start="2018-01-01", end=None):
    """Download adjusted close prices from Yahoo Finance using yfinance."""
    data = yf.download(tickers, start=start, end=end, auto_adjust=True, progress=False)
    if isinstance(data.columns, pd.MultiIndex):
        prices = data["Close"].copy()
    else:
        prices = data[["Close"]].rename(columns={"Close": tickers if isinstance(tickers, str) else tickers[0]})
    return prices.dropna(how="all")


def add_return_features(prices):
    """Create daily returns and common rolling risk/return features."""
    returns = prices.pct_change()
    features = pd.DataFrame(index=prices.index)
    if isinstance(prices, pd.Series):
        px = prices
    else:
        px = prices.iloc[:, 0]
    features["return_1d"] = px.pct_change()
    features["return_5d"] = px.pct_change(5)
    features["return_21d"] = px.pct_change(21)
    features["ma_50"] = px.rolling(50).mean()
    features["ma_200"] = px.rolling(200).mean()
    features["vol_21d_ann"] = features["return_1d"].rolling(21).std() * np.sqrt(252)
    features["drawdown"] = px / px.cummax() - 1
    return features


def max_drawdown(equity_curve):
    return (equity_curve / equity_curve.cummax() - 1).min()


def performance_summary(strategy_returns):
    strategy_returns = strategy_returns.dropna()
    equity = (1 + strategy_returns).cumprod()
    ann_return = strategy_returns.mean() * 252
    ann_vol = strategy_returns.std() * np.sqrt(252)
    sharpe = ann_return / ann_vol if ann_vol != 0 else np.nan
    return {
        "annual_return": ann_return,
        "annual_volatility": ann_vol,
        "sharpe_ratio": sharpe,
        "max_drawdown": max_drawdown(equity),
        "number_of_days": len(strategy_returns),
    }
