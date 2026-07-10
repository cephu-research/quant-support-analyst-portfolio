# Quant Support Analyst Portfolio Starter

This public portfolio is built to demonstrate practical skills for roles such as **Quantitative Support Analyst**, **Investment Analyst**, **Portfolio Analyst**, and **Financial Data Analyst**.

The projects focus on what trading and investment teams usually value:

- Turning a market question into a testable hypothesis
- Downloading and cleaning market data
- Building clear metrics and dashboards
- Testing simple signals without overclaiming predictive power
- Communicating conclusions in plain English

> Data source: Yahoo Finance through the open-source `yfinance` package. This portfolio is for educational and research purposes only, not investment advice.

## Projects

| Notebook | Project | Recruiter signal |
|---|---|---|
| `01_market_regime_dashboard.ipynb` | SPY/QQQ/VIX regime dashboard | Python, yfinance, risk metrics, visual thinking |
| `02_cross_asset_momentum_screener.ipynb` | ETF momentum and risk screener | Feature engineering, ranking, clean investment reasoning |
| `03_simple_backtest_signal.ipynb` | Trend-following signal and backtest | Hypothesis testing, backtesting discipline, performance metrics |

## Suggested repo structure

```text
quant-support-analyst-portfolio-starter/
├── notebooks/
│   ├── 01_market_regime_dashboard.ipynb
│   ├── 02_cross_asset_momentum_screener.ipynb
│   └── 03_simple_backtest_signal.ipynb
├── src/
│   └── market_utils.py
├── app/
│   └── streamlit_app.py
├── requirements.txt
├── .gitignore
└── README.md
```

## How to run in Google Colab

Open a notebook and run:

```python
!pip install yfinance plotly streamlit -q
```

## How to push to GitHub from Colab

```bash
!git clone https://github.com/YOUR_USERNAME/quant-support-analyst-portfolio.git
%cd quant-support-analyst-portfolio

# Upload/copy notebooks into this repo folder, then:
!git status
!git add .
!git commit -m "Add first quant support analyst portfolio notebooks"
!git push
```

## Positioning statement

I am a finance professional transitioning into investment analytics and quantitative support. My strength is combining accounting/controlling experience, market curiosity, Python notebooks, and practical dashboarding to help decision-makers turn questions into clean analysis.
