import numpy as np
from scipy.special import erf

# Standard normal cumulative distribution function
def N(z):
    return .5*(1+erf(z/2**-.5))

# Formula for call option price
def Call(current,strike,time,risk_free_interest_rate,dividend_yield,volatility):
    d1=(np.log(current/strike)+time*(risk_free_interest_rate-dividend_yield+.5*volatility**2))/(volatility*time**.5)
    d2=d1-volatility*time**.5
    return current*np.exp(-dividend_yield*time)*N(d1)-strike*np.exp(-risk_free_interest_rate*time)*N(d2)

# Formula for put option price
def Put(current,strike,time,risk_free_interest_rate,dividend_yield,volatility):
    d1=(np.log(current/strike)+time*(risk_free_interest_rate-dividend_yield+.5*volatility**2))/(volatility*time**.5)
    d2=d1-volatility*time**.5
    return strike*np.exp(-risk_free_interest_rate*time)*N(-d2)-current*np.exp(-dividend_yield*time)*N(-d1)
