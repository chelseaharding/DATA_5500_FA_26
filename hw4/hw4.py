import yfinance

# define function meanReversionStrategy
def meanReversionStrategy(): # will probably need arguments but I don't know what they are yet :)
    pass
    #    run strategy and output buys/sells, final profit, and final percentage returns
    #    return profit and returns


# define function simpleMovingAverageStrategy
def simpleMovingAverage(): # will probably need arguments but I don't know what they are yet
    pass
    #    run strategy and output buys/sells, final profit, and final percentage returns
    #    return profit and returns


# define function saveResults
def saveResults(results_dictionary):
    pass


# create list to store 10 tickers/stocks
tickers = ["TM", "WMT", "MAT", "GOOG", "AAPL", "TSLA", "ADBE", "COST", "NVDA", "NKE"]

# create dictionary called results to store prices, profits and return percentages
results = {}

# loop through the list of tickers/stocks

for ticker in tickers:
    # load prices from a file <ticker>.txt, and store them in the results dictionary with the key “<ticker>_prices”
    # file = open("hw3\TSLA.csv")
    # lines = file.readlines()
    # prices = []
    # for line in lines:
    #     prices.append(float(line))
    # file.close()

    # # reverse list (reverse dates)
    # prices = prices[::-1]
    # print(prices)

    stock_data = yfinance.download(ticker, period="1y")

    stock_data.to_csv("hw4/"+ticker+".csv", mode='w')





# call meanReversionStrategy(prices) and store the profit and returns in the results dictionary with the keys “<ticker>_mr_profit” and “<ticker>_mr_returns”

# call simpleMovingAverageStrategy(prices) and store the profit and returns in the results dictionary with the keys “<ticker>_sma_profit” and “<ticker>_sma_profit”

saveResults(results) # do this last and outside of for loop - save the results dictionary to a file called results.json