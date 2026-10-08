import random
import math
import numpy as np

# print(random.randint(1,6))

# suits = ['spades','clubs','diamonds','hearts']
faces = [2,3,4,5,6,7,8,9,10,'jack','queen','king','ace']

# cards = []

# for suit in suits:
#     for face in faces:
#         cards.append(f"{face} of {suit}")

# random.shuffle(cards)

# print(cards)

## math

# num = 10000

# print("log:", math.log(num))
# print("sin:", math.sin(num))
# print("tan:", math.tan(num))
# print("cos:", math.cos(num))
# print("sqrt:", math.sqrt(num))

"""
NumPy arrays are lighter and faster than python lists
They are homogenous
They are imutable
"""

prices = [123,175,143,345]
np_prices = np.array(prices)

# print(prices)
# print(np_prices)

random_numbers = np.random.normal(0,1,10000)

# from matplotlib import pyplot as plt

# plt.hist(random_numbers)
# plt.savefig("/workspaces/DATA_5500_FA_26/in_class_code/histplot.jpg")

# print(random_numbers)

data = np.array([1,2,3,4,5])

# print("mean:", np.mean(data))
# print("median:", np.median(data))
# print("std:", np.std(data))

file_path = "in_class_code/AAPL.2023.txt"

with open(file_path, 'r') as file:
    lines = file.readlines()

# print(lines)

# Create an empty array of the correct size
prices = np.zeros(len(lines))

# Populate the array with our prices
for i in range(len(lines)):
    prices[i] = lines[i]

# print(prices)

# calculate a simpler moving average
# total_avg = sum(prices) / len(prices)
# print("total_avg:", total_avg)

# five_day_avg = (prices[0] + prices[1] + prices[2] + prices[3] + prices[4]) / 5

# print("five_day_avg:", five_day_avg)

for i in range(len(prices)):
    if i <= 4:
        continue
    moving_five_day_avg = (prices[i] + prices[i-1] + prices[i-2] + prices[i-3] + prices[i-4]) / 5
    print(moving_five_day_avg)