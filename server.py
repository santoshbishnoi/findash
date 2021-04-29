from kiteconnect import KiteConnect

import pandas as pd

# collecting keys 
from config import api_key, api_secret, request_token, access_token


kite = KiteConnect(api_key=api_key)
# print(kite.login_url())

# data = kite.generate_session(request_token, api_secret=api_secret)
# print(data)

kite.set_access_token(access_token)



def return_data():
    data=kite.historical_data("738561", "2021-04-17 09:15:00", "2021-04-28 15:30:00", "5minute")
    df=pd.DataFrame.from_dict(data)
    return df
# print(type(data[0]['date']))
# print(len(data))
# print(df)

# print(kite.login_url())

# print(kite.ohlc("NSE:INFY"))