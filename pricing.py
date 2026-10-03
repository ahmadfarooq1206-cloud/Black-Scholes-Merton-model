import bsm
import greeks
import numpy as np
import pandas as pd
import yfinance as yf
from scipy.special import erf

# Acquires asset information
ticker=input('Please enter the ticker for the stock on Yahoo Finance you would like an option for? ')
data=yf.download(ticker,period='1y',multi_level_index=False)
S=round(float(data['Close'].tail(1).to_numpy()[0]),2) #type:ignore

# Dividend yield value
tick=yf.Ticker(ticker)
try:
    q=tick.info['dividendYield']/100
except KeyError:
    q=0

# Calculations for annualised historical volatility
df=pd.DataFrame(data)
df['log_returns']=np.log(df['Close']/df['Close'].shift(1))
o=df['log_returns'].std()*252**.5

# User input for strike price, time until maturity and risk free interest rate
K=float(input(f'The current price of {ticker} is {S}.\nWhat strike price would you like? '))
t=float(input(f'How long, as a decimal in years, would you like to hold your {ticker} option for? '))
r=float(input(f'Enter the risk free interest rate of the currency {ticker} is denominated in as a decimal '))

# Black-Scholes-Merton model inputs
d1=(np.log(S/K)+t*(r-q+.5*o**2))/(o*t**.5)
d2=d1-o*t**.5

# Greeks
option_call_delta=greeks.Call_Delta(q,t,d1)
option_put_delta=greeks.Put_Delta(q,t,d1)
option_gamma=greeks.Gamma(S,q,t,o,d1)
option_call_theta=greeks.Call_Theta(S,K,t,r,q,o,d1,d2)
option_put_theta=greeks.Put_Theta(S,K,t,r,q,o,d1,d2)
option_vega=greeks.Vega(S,q,t,d1)
option_call_rho=greeks.Call_Rho(K,t,r,d2)
option_put_rho=greeks.Put_Rho(K,t,r,d2)

# Results
call_price,put_price=bsm.Call(S,K,t,r,q,o).round(2),bsm.Put(S,K,t,r,q,o).round(2)
print(f'Call Price: {call_price}')
print(f'Put Price: {put_price}\n')
print(f'Call Delta: {option_call_delta}')
print(f'Put Delta: {option_put_delta}')
print(f'Gamma: {option_gamma}')
print(f'Call Theta: {option_call_theta}')
print(f'Put Theta: {option_put_theta}')
print(f'Vega: {option_vega}')
print(f'Call Rho: {option_call_rho}')
print(f'Put Rho: {option_put_rho}')
