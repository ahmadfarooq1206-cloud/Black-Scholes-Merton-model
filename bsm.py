import numpy as np
from scipy.special import erf

def Call(current,strike,time,risk_free_interest_rate,dividend_yield,volatility):
    def N(x):
        return 0.5*(1+erf(x/2**0.5))
    d1=(np.log(current/strike)+time*(risk_free_interest_rate-dividend_yield+0.5*volatility**2))/(volatility*time**0.5)
    d2=d1-volatility*time**0.5
    return current*np.exp(-dividend_yield*time)*N(d1)-strike*np.exp(-risk_free_interest_rate*time)*N(d2)

def Put(current,strike,time,risk_free_interest_rate,dividend_yield,volatility):
    def N(x):
        return 0.5*(1+erf(x/2**0.5))
    d1=(np.log(current/strike)+time*(risk_free_interest_rate-dividend_yield+0.5*volatility**2))/(volatility*time**0.5)
    d2=d1-volatility*time**0.5
    return strike*np.exp(-risk_free_interest_rate*time)*N(-d2)-current*np.exp(-dividend_yield*time)*N(-d1)
