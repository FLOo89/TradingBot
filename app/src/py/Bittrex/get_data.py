# import requests
# import time
# import pandas as pd
# 
# nonce = time.time()
# r = requests.get("https://api.bittrex.com/api/v1.1/public/getmarketsummary?market=btc-neo")
# print(r) 
import os
import pandas as pd

data_path = os.getcwd() + "\\src\\data\\BTC_NEO_100.csv"
print(data_path)
data = pd.read_csv(data_path, delimiter = ",")
data = data.drop('Unnamed: 0', axis=1)

