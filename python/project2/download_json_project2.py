import time
import requests
import json
"""This Script is meant to download the last 24 hours woth of transactions 
from poloniex.com's api. It will output a json file in the current directory
"""
#numbers: 43200:12h
start_time = str(int(time.time()) - 86400)
url = re.sub("''", start_time, 
             "https://poloniex.com/public?command=returnChartData&" + 
             "currencyPair=USDT_ETH&" +
             "start=''&end=9999999999&period=1800")

s = requests.session()
r = s.get(url)

data = json.loads(r.content)
with open("USDT_ETH24H.json", "wb") as f:
    f.write(r.content)
print("Output USDT_ETH24H.json to this script's directory")
