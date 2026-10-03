bsm.py is a pythonic implementation of the Black Scholes Merton pricing model for options.

greeks.py calculates the Greeks which are various measures of sensitivity to the input variables of the Black-Scholes-Merton model.

pricing.py uses the code in bsm.py and greeks.py alongside live data from Yahoo Finance to give call and put prices for listed stocks as well as their greeks.

variation.ipynb plots the greeks and how they behave as the variables they measure change.
