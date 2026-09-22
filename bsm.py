import numpy as np
from scipy.integrate import quad

def N(z):
    f=lambda x: (2*np.pi)**-.5*np.exp(-.5*x**2)
    return quad(f,-np.inf,z)[0]

def Call(current,strike,time,risk_free_interest_rate,dividend_yield,volatility):
    d1=(np.log(current/strike)+time*(risk_free_interest_rate-dividend_yield+0.5*volatility**2))/(volatility*time**0.5)
    d2=d1-volatility*time**0.5
    return current*np.exp(-dividend_yield*time)*N(d1)-strike*np.exp(-risk_free_interest_rate*time)*N(d2)

def Put(current,strike,time,risk_free_interest_rate,dividend_yield,volatility):
    d1=(np.log(current/strike)+time*(risk_free_interest_rate-dividend_yield+0.5*volatility**2))/(volatility*time**0.5)
    d2=d1-volatility*time**0.5
    return strike*np.exp(-risk_free_interest_rate*time)*N(-d2)-current*np.exp(-dividend_yield*time)*N(-d1)
