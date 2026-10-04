import numpy as np

# Monte Carlo simulation for call option pricing
def bsm_call_monte_carlo(S,K,t,r,q,o):
    z=np.random.standard_normal(1000000)
    St=S*np.exp(t*(r-q-.5*o**2)+o*t**.5*z)
    payoff=np.maximum(St-K,0)
    call_price=np.exp(-r*t)*np.mean(payoff)
    return call_price

# Monte Carlo simulation for put option pricing
def bsm_put_monte_carlo(S,K,t,r,q,o):
    z=np.random.standard_normal(1000000)
    St=S*np.exp(t*(r-q-.5*o**2)+o*t**.5*z)
    payoff=np.maximum(K-St,0)
    put_price=np.exp(-r*t)*np.mean(payoff)
    return put_price
