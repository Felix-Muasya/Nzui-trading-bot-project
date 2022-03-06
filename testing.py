# getting financial data from yahoo
import pandas as pd
import yfinance as yf
from yahoofinancials import YahooFinancials

btcusd = yf.download('BTC-USD', start = '2022-01-01', end = '2022-02-02', progress = False)
price_data = pd.DataFrame (btcusd)
price_data.to_csv('C:\\Users\\USER\\Desktop\\Rada.csv')

print(price_data.corr())