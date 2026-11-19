import requests
import json

url = "https://api.datamuse.com/words?rel_trg=cow"

request = requests.get(url)
cow_json = json.loads(request.text)
# print(cow_json)

for dictionary in cow_json:
    if dictionary["word"] == "cheese":
        print(dictionary["word"], dictionary["score"])


# financial url API

url2 = "https://financialmodelingprep.com/stable/historical-price-eod/full?symbol=aapl&from=2024-09-23&to=2026-11-19&apikey=x8xwEwpa1ujKsPAqiLDeXut6G2j11qQ1"

request = requests.get(url2)
stock_json = json.loads(request.text)
# print(stock_json)

# construct a csv file that looks like homework 4

date_key = "date"
close_key = "close"

# open .csv file
file = open("/workspaces/DATA_5500_FA_26/in_class_code/AAPL.csv", "w")

lines = []

# there's always a loop - for loop
for dictionary in stock_json:
    # interact with key value pairs
    # print(dictionary["date"], dictionary["close"])
    # string concatenation
    lines.append(dictionary["date"]+", "+ str(dictionary["close"])+"\n")
    # print(csv_line)
# reverse the order of our data
lines = lines[::-1]
# write to a file
file.writelines(lines)


""" 
https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=aapl&apikey="+api_key
"""
