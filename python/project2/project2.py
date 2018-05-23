import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import mpl_finance as mpl_f
import matplotlib.dates as mpl_d
import time
import requests
import json
import re
"""This script downloads a json file from polonix.com's api conatining the 
last 24 hours worth of ethereum transactions, then 
displays the gathered data in a candlesick chart. The script must 
be run on a system with a desktop environment to run correctly. """
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

df = pd.read_json("USDT_ETH24H.json")
df.index = df['date']
df['date']=mpl_d.date2num(df.index.to_pydatetime())
df.index = range(0,len(df))
df = df[['date', 'open', 'high', 'low', 'close', 
         'quoteVolume', 'volume', 'weightedAverage']]
fig, ax = plt.subplots()
fig.subplots_adjust(bottom=0.2)
#ax.xaxis.set_minor_locator(mpl_d.MinuteLocator())
ax.xaxis.set_major_locator(mpl_d.HourLocator())
ax.xaxis.set_major_formatter(mpl_d.DateFormatter('%H:%M'))
ax.set_xlabel("Time", fontsize=12)
ax.set_ylabel("Price ($)", fontsize=12)
ax.set_title("Etherium price over the past 24 hours")

i = 0
candleArray = []
while i < len(df):
    newline = df['date'][i], df['open'][i], df['high'][i], df['low'][i], df['close'][i]
    candleArray.append(newline)
    i += 1
mpl_f.candlestick_ohlc(ax, candleArray, width=0.006,
                       colorup='g',
                       colordown='r')

ax.xaxis_date()
ax.autoscale_view()
plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')
#plt.legend(loc='best')
plt.show()

