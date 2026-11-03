"""
Dictionary
"""

colors = ["aggie blue", "fighting white", "thistle"]
information = ["Thursday", 9, False, 3.14]

adam = {}
adam["full_name"] = "Adam Jessen"
adam["age"] = 23
adam["major"] = "MMIS"
adam["classes"] = ["DATA5500", "DATA5300", "DATA5400"]
adam["car"] = {"make":"Buick", "model":"Lacrosse", "year": 2006, "transmission":"Automatic", "color":"gray"}

# entire dictionary
# print(adam)

# look up specific values
print(adam["major"])  #MMIS
print(type(adam["classes"]))
print(adam["classes"][2])
print(adam["car"].keys())
print(adam["car"]["color"])

# mileage of the car
adam["car"]["mileage"] = 195000
print(adam["car"].keys())

adam["classes"].append("PE1680")
print(adam["classes"])

# json


"""
Write a program that asks the user the following:

Survey information (a mixture of strings and numbers)
 - How many years have you lived in Cache Valley (enter a float)?
 - What is your favorite color (enter a string)?
 - What is your favorite programming language (enter a string)?
Store the user's answers in a Dictionary
Loop through the dictionary and print all the values
"""

survey = {}
survey["cache_years"] = float(input("How many years have you lived in CV: "))
survey["fav_color"] = input("What is your favorite color: ")
survey["fav_programming_lang"] = input("What is your favorite programming languge: ")

for key in survey.keys():
    print("key:", key, "\n", "value:", survey[key])