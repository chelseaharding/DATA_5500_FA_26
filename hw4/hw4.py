import json
import pandas as pd

# define function meanReversionStrategy
def meanReversionStrategy(prices): # will probably need arguments but I don't know what they are yet :)
    pass
    #    run strategy and output buys/sells, final profit, and final percentage returns
    #    return profit and returns


# define function simpleMovingAverageStrategy
def simpleMovingAverage(prices): # will probably need arguments but I don't know what they are yet
    pass
    #    run strategy and output buys/sells, final profit, and final percentage returns
    #    return profit and returns


# define function saveResults
def saveResults(results_dictionary):
    pass


# create list to store 10 tickers/stocks
tickers = ["TSLA", "NVDA"]

# create dictionary called results to store prices, profits and return percentages
results = {}

# loop through the list of tickers/stocks

for ticker in tickers:
    # load prices from a file <ticker>.txt, and store them in the results dictionary with the key “<ticker>_prices”
    file = pd.read_csv("/workspaces/DATA_5500_FA_26/hw4/"+ticker+".csv")
    stock_prices = file["Close/Last"] #pandas series (one dimensional)
    # print(stock_prices)
    prices = [] #new list to store our prices from the pandas series
    for item in stock_prices:
        prices.append(float(item.replace("$", "")))
    # print(prices)
    
    # reverse list (reverse dates)
    prices = prices[::-1]
    # print(prices)

    # call meanReversionStrategy(prices) and store the profit and returns in the results dictionary with the keys “<ticker>_mr_profit” and “<ticker>_mr_returns”
    meanReversionStrategy(prices)

    # call simpleMovingAverageStrategy(prices) and store the profit and returns in the results dictionary with the keys “<ticker>_sma_profit” and “<ticker>_sma_profit”
    simpleMovingAverage(prices)

saveResults(results) # do this last and outside of for loop - save the results dictionary to a file called results.json