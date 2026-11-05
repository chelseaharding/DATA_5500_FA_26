# json

# codespaces were not working so the paths are broken 😃

import json

thistle = {}
thistle['color'] = 'cream'
thistle['is_cute?'] =True
thistle['rating_out_of_10'] = 9999999999
thistle['thistle_facts'] = {
    'how_many_thistles?' : 2,
    'location' : 'south basin'
} 

# save thistle.json
with open("thistle.json",'w') as file:
    json.dump(thistle, file, indent=4)

# load in thistle.json
thistle_2 = json.load(
    open("thistle.json")
)


"""
Homework 4
"""
import pandas as pd

def meanReversion(prices):
    # comparing moving avg 
    buy          = 0
    first_buy    = 0
    total_profit = 0

    for i in range(5, len(prices)):
        current_price   = prices[i]
        moving_avg      = sum(prices[i-5:i]) / 5

        if current_price < (moving_avg  * 0.98) and buy == 0: #0.98 for 21 # 0.96 for 22
                print("buying at: ", "\t", round(current_price, 3), "iteration", i)
                buy = current_price
                if first_buy == 0:
                    first_buy = buy
        elif current_price > (moving_avg * 1.02) and buy != 0: #1.02 for 21 #1.04 for 22
            print("selling at: ", "\t", round(current_price, 3))
            trade_profit = current_price - buy
            print("trade profit: ", "\t", round(trade_profit, 2))
            total_profit += trade_profit
            buy = 0
        else:
            pass

    if first_buy == 0:
        print("Never Traded Stock")
        return 0, 0

    percent_return = (total_profit / first_buy) * 100
    return percent_return, total_profit

def simpleMovingAverage(prices):
     ...

def loadPrices(ticker):
     df = pd.read_csv(ticker + '.csv')
     prices = df['Close/Last'].apply(lambda x: float(x[1:]))
     prices = list(prices)[::-1]
     return prices


def saveResults(results_dictionary):
     with open('results.json','w') as file:
         json.dump(results_dictionary, file, indent=2)
         print("Results were saved to results.json")

prices = loadPrices('nke')

results_dict = {}

results_dict['nke_pct_return'], results_dict['nke_tot_profit'] = meanReversion(prices)

saveResults(results_dict)