import pandas as pd
import numpy as np
import yfinance as yf
from bsm import Call,Put

ticker=input('Please enter the ticker for the stock or ETF you would like an option for?')
data=yf.download(ticker,period='1y')
current=data['Close'].dropna().to_numpy()[-1][0].round(2)

tick=yf.Ticker(ticker)
try:
    dividend_yield=tick.info['dividendYield']
except KeyError:
    dividend_yield=0

df=pd.DataFrame(data)
df['log_returns']=np.log(df['Close']/df['Close'].shift(1))
volatility=df['log_returns'].std()*252**0.5

strike=float(input(f'The current price of {ticker} is {current}.\nWhat strike price would you like? '))
time=float(input(f'How long, as a decimal in years, would you like to hold your {ticker} option for? '))
risk_free_interest_rate=float(input(f'Enter the risk free interest rate of the currency {ticker} is denominated in as a decimal '))

info=[current,strike,time,risk_free_interest_rate,dividend_yield,volatility]

call,put=Call(*info).round(2),Put(*info).round(2)
print(f'{ticker} Call Price: {call}')
print(f'{ticker} Put Price: {put}')
