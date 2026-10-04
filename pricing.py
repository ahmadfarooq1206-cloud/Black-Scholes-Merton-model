import bsm
import bsm_mc
import greeks
import numpy as np
import pandas as pd
import yfinance as yf

ticker=input('Please enter the ticker for the stock on Yahoo Finance you would like an option for?  ')
data=yf.download(ticker,period='1y',multi_level_index=False)
S=round(float(data['Close'].tail(1).to_numpy()[0]),2) #type:ignore

tick=yf.Ticker(ticker)
try:
    q=tick.info['dividendYield']/100
except KeyError:
    q=0

df=pd.DataFrame(data)
df['log_returns']=np.log(df['Close']/df['Close'].shift(1))
o=df['log_returns'].std()*252**.5

K=float(input(f'The current price of {ticker} is {S}.\nWhat strike price would you like?    '))
t=float(input(f'How long, as a decimal in years, would you like to hold your {ticker} option for?   '))
r=float(input(f'Enter the risk free interest rate of the currency {ticker} is denominated in as a decimal   '))

d1=(np.log(S/K)+t*(r-q+.5*o**2))/(o*t**.5)
d2=d1-o*t**.5

option_call_delta=greeks.Call_Delta(q,t,d1).round(5)
option_put_delta=greeks.Put_Delta(q,t,d1).round(5)
option_gamma=greeks.Gamma(S,q,t,o,d1).round(5)
option_call_theta=greeks.Call_Theta(S,K,t,r,q,o,d1,d2).round(5)
option_put_theta=greeks.Put_Theta(S,K,t,r,q,o,d1,d2).round(5)
option_vega=greeks.Vega(S,q,t,d1).round(5)
option_call_rho=greeks.Call_Rho(K,t,r,d2).round(5)
option_put_rho=greeks.Put_Rho(K,t,r,d2).round(5)

call_price=bsm.Call(S,K,t,r,q,o).round(2)
put_price=bsm.Put(S,K,t,r,q,o).round(2)
simulated_call_price=bsm_mc.bsm_call_monte_carlo(S,K,t,r,q,o).round(2)
simulated_put_price=bsm_mc.bsm_put_monte_carlo(S,K,t,r,q,o).round(2)
call_discrepancy=(100*np.abs(call_price-simulated_call_price)/call_price).round(3)
put_discrepancy=(100*np.abs(put_price-simulated_put_price)/put_price).round(3)

print(f'\nCall Price: {call_price}\nMonte Carlo simulated call price: {simulated_call_price}')
print(f'Call price discrepancy: {call_discrepancy}%\n')
print(f'Put Price: {put_price}\nMonte Carlo simulated put price: {simulated_put_price}')
print(f'Put price discrepancy: {put_discrepancy}%\n')

print(f'Deltas:\nCall: {option_call_delta}  Put: {option_put_delta}')
print(f'Gamma:\n{option_gamma}')
print(f'Thetas:\nCall: {option_call_theta}  Put: {option_put_theta}')
print(f'Vega:\n{option_vega}')
print(f'Rhos:\nCall: {option_call_rho}  Put: {option_put_rho}\n')
