"""
Application Programming Interface
"""
import requests
import json

# url = "https://v2.jokeapi.dev/joke/Any"

# request = requests.get(url)
# # print(request) # I have a good request
# joke_json = json.loads(request.text)
# print(joke_json)

# fun part: set up a loop to continuously ask user if they want to hear a joke and print one out if they do :)

# while True:
#     get_joke = input("Do you want to hear a joke? (y/n) ")
#     request = requests.get(url)
#     joke_json = json.loads(request.text)
#     if get_joke == "y":
#         if joke_json["type"] == "twopart":
#             print(joke_json["setup"])
#             input() #user press any key to hear the delivery
#             print(joke_json["delivery"])
#         else:
#             print(joke_json["joke"])
#     elif get_joke == "n":
#         break
#     else: 
#         print("Please enter 'y' or 'n'")

url = "https://v2.jokeapi.dev/joke/Any"

request = requests.get(url)
joke_json = json.loads(request.text)

for flag in joke_json["flags"].keys():
    #safe jokes
    if flag == "political" or flag == "religious":
        if joke_json["type"] == "twopart":
            print(joke_json["setup"])
            print(joke_json["delivery"])
        else:
            print(joke_json["joke"])
        break #if it hits political or religious 


