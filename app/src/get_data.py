import requests
import time
import pandas as pd

nonce = time.time()
r = requests.get("https://bittrex.com/api/v1.1/public/getmarkethistory?market=BTC-NEO")
tickets = pd.DataFrame()
print(r['results']) 
