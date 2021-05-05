from kiteconnect import KiteConnect

import pandas as pd
import datetime as dt

# collecting keys 
from config import api_key, api_secret, request_token, access_token

#accessing the instrument tokens
from src.nse_constants import nifty50_tokens


#accessing tokens for the API
kite = KiteConnect(api_key=api_key)
# print(kite.login_url())

# data = kite.generate_session(request_token, api_secret=api_secret)
# print(data['access_token'])

kite.set_access_token(access_token)


#used to determine status of market 
market_open=False



opening_time=dt.time(hour=9,minute=15, second=0, microsecond=0 )
closing_time=dt.time(hour=15,minute=30, second=0, microsecond=0 )

current_datetime=dt.datetime.now()
current_time=current_datetime.time()

if current_time>opening_time and current_time<closing_time:
    market_open=True


if not(market_open):
    if ((current_datetime.weekday()==0) and (dt.datetime.now().time() < dt.time(hour=9,minute=15, second=0, microsecond=0))):
        chart_end_time=dt.date.today()-dt.timedelta(days=3)
    elif current_datetime.weekday()<5:
        if(dt.datetime.now().time() > dt.time(hour=15,minute=30, second=0)) and (dt.datetime.now().time() < dt.time(hour=23,minute=59, second=59, microsecond=0)):
                chart_end_time=dt.date.today()
        if(dt.datetime.now().time() < dt.time(hour=9,minute=15, second=0, microsecond=0)):
                chart_end_time=dt.date.today()-dt.timedelta(days=1)
    elif current_datetime.weekday()==5:
        chart_end_time=dt.date.today()-dt.timedelta(days=1)
    elif current_datetime.weekday()==6:
        chart_end_time=dt.date.today()-dt.timedelta(days=2)

    chart_range=dt.timedelta(days=1)
    chart_start_time=chart_end_time-chart_range







def return_data():
    data=kite.historical_data(nifty50_tokens["RELIANCE INDUSTRIES"], chart_start_time, chart_end_time, "5minute")
    df=pd.DataFrame.from_dict(data)
    # print(df)
    return df
# print(type(data[0]['date']))
# print(len(data))
# print(df)

# print(kite.login_url())

# print(kite.ohlc("NSE:INFY"))

# print(kite.historical_data(nifty50_tokens["RELIANCE INDUSTRIES"], "2021-05-04", "2021-05-05", "5minute"))
# data=kite.historical_data(nifty50_tokens["RELIANCE INDUSTRIES"], chart_start_time, chart_end_time, "minute")
# df=pd.DataFrame.from_dict(data)
# print(df)