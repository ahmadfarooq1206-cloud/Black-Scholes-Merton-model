from scipy.special import erf
import numpy as np

pi=np.pi

def N(z):
    return .5*(1+erf(z/2**.5))

def dN(z):
    return (2*pi)**-.5*np.exp(-.5*z**2)

def d1(S,K,t,r,q,o):
    return (np.log(S/K)+t*(r-q+.5*o**2))/(o*t**.5)

def d2(d1,o,t):
    return d1-o*t**.5

def Call_Delta(q,t,d1):
    return np.exp(-q*t)*N(d1)

def Put_Delta(q,t,d1):
    return -np.exp(-q*t)*N(-d1)

def Gamma(S,q,t,o,d1):
    return np.exp(-q*t)*dN(d1)/(S*o*t**.5)

def Call_Theta(S,K,t,r,q,o,d1,d2):
    return 1/252*(-((S*o*np.exp(-q*t)*dN(d1))/(2*t**.5))-r*K*np.exp(-r*t)*N(d2)+q*S*np.exp(-q*t)*N(d1))

def Put_Theta(S,K,t,r,q,o,d1,d2):
    return 1/252*(-((S*o*np.exp(-q*t)*dN(d1))/(2*t**.5))+r*K*np.exp(-r*t)*N(d2)-q*S*np.exp(-q*t)*N(d1))

def Vega(S,q,t,d1):
    return .01*S*np.exp(-q*t)*t**.5*dN(d1)

def Call_Rho(K,t,r,d2):
    return .01*K*t*np.exp(-r*t)*N(d2)

def Put_Rho(K,t,r,d2):
    return -.01*K*t*np.exp(-r*t)*N(-d2)
