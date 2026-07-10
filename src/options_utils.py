import numpy as np
import pandas as pd


def option_payoff_at_expiry(underlying_prices, option_type, strike, premium, quantity=1):
    """Return payoff at expiry for one option leg.

    option_type: 'call' or 'put'
    premium: positive number paid/received per contract unit
    quantity: positive for long, negative for short
    """
    S = np.asarray(underlying_prices)
    if option_type.lower() == 'call':
        intrinsic = np.maximum(S - strike, 0)
    elif option_type.lower() == 'put':
        intrinsic = np.maximum(strike - S, 0)
    else:
        raise ValueError("option_type must be 'call' or 'put'")
    return quantity * (intrinsic - premium)


def strategy_payoff(underlying_prices, legs):
    total = np.zeros_like(np.asarray(underlying_prices), dtype=float)
    for leg in legs:
        total += option_payoff_at_expiry(
            underlying_prices,
            option_type=leg['type'],
            strike=leg['strike'],
            premium=leg['premium'],
            quantity=leg['quantity'],
        )
    return total


def summarize_payoff(underlying_prices, payoff):
    payoff = np.asarray(payoff)
    return pd.Series({
        'max_profit_in_range': payoff.max(),
        'max_loss_in_range': payoff.min(),
        'breakeven_count_in_range': np.sum(np.diff(np.sign(payoff)) != 0),
        'best_price_in_range': underlying_prices[payoff.argmax()],
        'worst_price_in_range': underlying_prices[payoff.argmin()],
    })
