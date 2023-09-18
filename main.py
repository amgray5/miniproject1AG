#%%
# INF601 - Advanced Programming in Python
# Austin Gray
# Mini Project 1

import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

def getClosing(ticker):
    #get the closing price for the last 10 trading days
    stock = yf.Ticker(ticker)

    # get historical market data
    hist = stock.history(period='10d')

    closingList = []

    for price in hist['Close']:
        closingList.append(round(price, 2))

    return closingList

stocks = ['AMD', 'CSCO', 'MSFT', 'LOGI', 'JPM']

for stock in stocks:
    stockClosing = np.array(getClosing(stock))
    days = list(range(1, len(stockClosing)+1))

    # This plots the graph
    plt.plot(days, stockClosing)

    # Get our min and max for Y
    prices = getClosing(stock)
    prices.sort()
    low_price  = prices[0]
    high_price = prices[-1]

    # Set our X axis min and max
    # form [xmin, xmax, ymin, ymax]
    plt.axis([1, 10, low_price-2, high_price+2])

    # Set our labels for the graph
    plt.xlabel("Days")
    plt.ylabel('Closing Price')
    plt.title(f'Closing Price for {stock}')

    #saves images
    savefile = f'charts/{stock}.png'
    plt.savefig(savefile)

    #Finally show the graph
    plt.show()


# %%
