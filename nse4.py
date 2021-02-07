import statistics
import pandas as pd
import nsepy
from nsepy import get_history as gh
import datetime as dt
import talib as ta
import numpy as np


tradingsymbol = 'NIFTY'
start = dt.date(2020,1,1)
end = dt.date(2021,2,5)

data = gh(tradingsymbol, start, end, index=True) # for index (nifty and bnf values
df = pd.DataFrame(data)
df.to_csv('nifty.csv')
#df1 = df.filter(['Symbol','Open', 'Close', 'High', 'Low', 'Volume'], axis=1)
rsi = ta.RSI(df['Close'], timeperiod=10)
df['RSI'] = rsi
adx = ta.ADX(df['High'], df['Low'], df['Close'], timeperiod=10)
df['adx'] = adx

condition = []

for i, j in zip(rsi, adx):
	if i > 50 and j > 20:
		k = "buy"
		
		
	elif i < 50 and j > 20:
		k = "sell"
		
	else:
		k = "neutral"
	condition.append(k)
df['condition'] = condition
print(df.tail(50))


# condition check for RSI and ADX
'''condition = []
Previousstage = 0
for i, j in zip(rsi, adx):
	if i > 50 and j > 20 and Previousstage != 1:
		k = "buy"
		Previousstage = 1
		
	elif i < 50 and j > 20 and Previousstage != -1:
		k = "sell"
		Previousstage = -1
	else:
		k = "neutral"
	condition.append(k)
df['condition'] = condition
print(df.tail(20))
'''