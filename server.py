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
data=kite.historical_data(nifty50_tokens["RELIANCE INDUSTRIES"],"2015-01-01", "2015-06-01", "15minute")
# print(data)
df=pd.DataFrame.from_dict(data)
# df=df.drop(df.columns[0], axis=1)
# print(df)

# Function to reterieve historical data points and store on local system
def data_to_csv():
    for key, value in nifty50_tokens.items():
        start_date = dt.datetime(2015, 1, 1)
        end_date=start_date+dt.timedelta(weeks=48)
        i=0
        while(end_date<dt.datetime(2021, 12, 12)):
            data=kite.historical_data(value,start_date,end_date, "day")
            df=pd.DataFrame.from_dict(data)
            if(i==0):
                df.to_csv("historical_data/1D/"+key+"1D.csv", mode="a", index=False)
            df.to_csv("historical_data/1D/"+key+"1D.csv", mode="a", header=False, index=False)
            start_date=end_date+dt.timedelta(days=1)
            end_date=start_date+dt.timedelta(weeks=48)
            i=i+1




    

def SMA(df, base, target, period):
    """
    Function to compute Simple Moving Average (SMA)
    
    Args :
        df : Pandas DataFrame which contains ['date', 'open', 'high', 'low', 'close', 'volume'] columns
        base : String indicating the column name from which the SMA needs to be computed from
        target : String indicates the column name to which the computed data needs to be stored
        period : Integer indicates the period of computation in terms of number of candles
        
    Returns :
        df : Pandas DataFrame with new column added with name 'target'
    """

    df[target] = round(df[base].rolling(window=period).mean(), 2)
    df[target].fillna(0, inplace=True)

    return df


def EMA(df, base, target, period, alpha=False):
    """
    Function to compute Exponential Moving Average (EMA)
    
    Args :
        df : Pandas DataFrame which contains ['date', 'open', 'high', 'low', 'close', 'volume'] columns
        base : String indicating the column name from which the EMA needs to be computed from
        target : String indicates the column name to which the computed data needs to be stored
        period : Integer indicates the period of computation in terms of number of candles
        alpha : Boolean if True indicates to use the formula for computing EMA using alpha (default is False)
        
    Returns :
        df : Pandas DataFrame with new column added with name 'target'
    """

    con = pd.concat([df[:period][base].rolling(window=period).mean(), df[period:][base]])
    
    if (alpha == True):
        # (1 - alpha) * previous_val + alpha * current_val where alpha = 1 / period
        df[target] = round(con.ewm(alpha=1 / period, adjust=False).mean(),2)
    else:
        # ((current_val - previous_val) * coeff) + previous_val where coeff = 2 / (period + 1)
        df[target] = round(con.ewm(span=period, adjust=False).mean(),2)
    
    df[target].fillna(0, inplace=True)
    return df

SMA_df= SMA(df, "close", "Sma", 14)
# print(SMA_df)
EMA_50=EMA(df, "close", "EMA50", 50)
# print(EMA_50)

# f=open("RELIANCE_15M", "w")
# f.write(EMA_50)
# f.close()

# EMA_50.to_csv("sa/RELIANCE15M.csv", mode="a", header=False)
# EMA_50.to_csv("RELIANCE15M.csv",index=False)