from kiteconnect import KiteConnect

import pandas as pd
import datetime as dt

# collecting keys 
from config import api_key, api_secret, request_token, access_token

#accessing the instrument tokens
from src.nse_constants import nifty50_tokens


kite = KiteConnect(api_key=api_key)
# print(kite.login_url())

# data = kite.generate_session(request_token, api_secret=api_secret)
# print(data['access_token'])

kite.set_access_token(access_token)
# print(nifty50_tokens)

current_time=dt.datetime.now()
hours= 5
hours_added=dt.timedelta(hours=hours)
futuretime=current_time+hours_added

def return_data():
    data=kite.historical_data(nifty50_tokens["RELIANCE INDUSTRIES"], "2021-04-30 13:15:00", futuretime, "minute")
    df=pd.DataFrame.from_dict(data)
    return df
# print(type(data[0]['date']))
# print(len(data))
# print(df)

# print(kite.login_url())

# print(kite.ohlc("NSE:INFY"))