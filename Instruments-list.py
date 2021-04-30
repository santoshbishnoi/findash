import pandas as pd

nifty50df=pd.read_csv("ind_nifty50list.csv")

instrumentsdf=pd.read_csv("instruments.csv")

symbol_li=list(nifty50df['Symbol'])
# print(symbol_li)

instrumentsdict={}

for i in symbol_li:
    for j in instrumentsdf.index:
        if instrumentsdf["tradingsymbol"][j]==i and instrumentsdf["exchange"][j]=="NSE":
            instrumentsdict[instrumentsdf["name"][j]]=instrumentsdf["instrument_token"][j]

print(instrumentsdict)

with open("instruments-list.txt", 'w') as file:
    file.write(json.dumps(instrumentsdict))
            

# for i in nifty50df.index:
#     print(i)

# print(instrumentsdf["tradingsymbol"][20])