"""
Homework 3 - Stock Market Trading
"""
# normal way to read prices in from file
file = open("/workspaces/DATA_5500_FA_26/hw3/TSLA.csv")
lines = file.readlines()
prices = []
for line in lines:
    prices.append(float(line))

# list comprehension
prices = [float(line) for line in open("/workspaces/DATA_5500_FA_26/hw3/TSLA.csv").readlines()]
print(prices)

# reverse list (reverse dates)
prices = prices[::-1]