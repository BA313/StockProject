import matplotlib.pyplot as plt
from importData import *


tickerlist = ['SPY', 'TWTR', 'TSLA', 'PYPL', 'BTC-USD', 'ETSY']
tickers = "SPY TWTR TSLA PYPL BTC-USD ETSY"
data = getData(tickers)

#plot data
figure, axis = plt.subplots(2, 3, figsize=(15, 9))
axis[0, 0].set_title(list[0])
axis[0, 1].set_title(list[1])
axis[0, 2].set_title(list[2])
axis[1, 0].set_title(list[3])
axis[1, 1].set_title(list[4])
axis[1, 2].set_title(list[5])
plt.subplots_adjust(hspace=0.5)
#print(data['SPY'])
data['SPY', 'close'].plot(ax=axis[0, 0], subplots=True)

#print(data['TWTR'])
data['TWTR', 'close'].plot(ax=axis[0, 1], subplots=True, color='r')

#print(data['TSLA'])
data['TSLA', 'close'].plot(ax=axis[0, 2], subplots=True, color='g')

#print(data['PYPL'])
data['PYPL', 'close'].plot(ax=axis[1, 0], subplots=True, color='y')

#print(data['BTC-USD'])
data['BTC-USD', 'close'].plot(ax=axis[1, 1], subplots=True, color='c')

#print(data['ETSY'])
data['ETSY', 'close'].plot(ax=axis[1, 2], subplots=True, color='b')

plt.show()

