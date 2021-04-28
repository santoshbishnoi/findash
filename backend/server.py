from kiteconnect import KiteConnect

from config import api_key, api_secret, request_token, access_token





kite = KiteConnect(api_key=api_key)

# data = kite.generate_session(request_token, api_secret=api_secret)
kite.set_access_token(access_token)

print(kite.orders())
# print(data)
