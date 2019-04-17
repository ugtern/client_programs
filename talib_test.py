import numpy
import talib
import requests
import json
import time

from matplotlib.finance import candlestick2_ohlc
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import datetime as datetime

start_time = time.time() - 24*60*60
resource = requests.get("https://poloniex.com/public?command=returnChartData&currencyPair=BTC_ETH&start=%s&end=9999999999&period=300" % start_time)
data = json.loads(resource.text)

quotes = {}
quotes['open']=numpy.asarray([item['open'] for item in data])
quotes['close']=numpy.asarray([item['close'] for item in data])
quotes['high']=numpy.asarray([item['high'] for item in data])
quotes['low']=numpy.asarray([item['low'] for item in data])

xdate=[datetime.datetime.fromtimestamp(item['date']) for item in data]

fig, ax = plt.subplots()

candlestick2_ohlc(ax,quotes['open'],quotes['high'],quotes['low'],quotes['close'],width=0.6)

ax.xaxis.set_major_locator(ticker.MaxNLocator(6))

def chart_date(x,pos):
    try:
        return xdate[int(x)]
    except IndexError:
        return ''

ax.xaxis.set_major_formatter(ticker.FuncFormatter(chart_date))

fig.autofmt_xdate()
fig.tight_layout()

plt.show()