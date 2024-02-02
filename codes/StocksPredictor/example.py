from pandas_datareader import data as web
from datetime import datetime
import yfinance as yf

yf.pdr_override()

symbol = "META"

start = datetime(2016,3,1)
end = datetime(2016, 3, 31)
sk = web.get_data_yahoo(tickers=symbol, start=start,end=end) # yf.download()
print(sk)