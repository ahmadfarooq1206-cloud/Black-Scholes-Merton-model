from scipy.special import erf
import numpy as np

pi=np.pi

# Standard normal cumulative function
def N(z):
    return .5*(1+erf(z/2**.5))

# Standard normal probability density function
def dN(z):
    return (2*pi)**-.5*np.exp(-.5*z**2)

# Black-Scholes-Merton model input
def d1(S,K,t,r,q,o):
    return (np.log(S/K)+t*(r-q+.5*o**2))/(o*t**.5)

# Black-Scholes-Merton model input
def d2(d1,o,t):
    return d1-o*t**.5

# Delta for call options
def Call_Delta(q,t,d1):
    return np.exp(-q*t)*N(d1)

# Delta for put options
def Put_Delta(q,t,d1):
    return -np.exp(-q*t)*N(-d1)

# Gamma for options
def Gamma(S,q,t,o,d1):
    return np.exp(-q*t)*dN(d1)/(S*o*t**.5)

# Theta for call options
def Call_Theta(S,K,t,r,q,o,d1,d2):
    return 1/252*(-((S*o*np.exp(-q*t)*dN(d1))/(2*t**.5))-r*K*np.exp(-r*t)*N(d2)+q*S*np.exp(-q*t)*N(d1))

# Theta for put options
def Put_Theta(S,K,t,r,q,o,d1,d2):
    return 1/252*(-((S*o*np.exp(-q*t)*dN(d1))/(2*t**.5))+r*K*np.exp(-r*t)*N(d2)-q*S*np.exp(-q*t)*N(d1))

# Vega for options
def Vega(S,q,t,d1):
    return .01*S*np.exp(-q*t)*t**.5*dN(d1)

# Rho for call options
def Call_Rho(K,t,r,d2):
    return .01*K*t*np.exp(-r*t)*N(d2)

# Rho for put options
def Put_Rho(K,t,r,d2):
    return -.01*K*t*np.exp(-r*t)*N(-d2)
