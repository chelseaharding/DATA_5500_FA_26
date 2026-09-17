# loops :)

age = 22

while age > 10:
    print("congrats")
    print("age:", age)
    age = age - 1
else:
    print("baby")


score = 0

while score < 27:
    print("you haven't won yet", score)
    score = score + 1
else:
    print("you won!", score)


# for loop
score = 0

for i in range(10):
    score = score + 1
    print(score)

print("total score", score)

# for looping over a range
for i in range(0, 20):
    print("i:", i)

# for loop over a list
colors = ["Aggie Blue", "Fighting White", "Sage Green"]

for color in colors:
    print("color:", color)

# for loop over a string
name = "Chelsea Harding"

for char in name:
    print(char)

"""
Guess the secret number

Import a random number
Have the user guess what the number is
If they get it wrong, tell them if they are too high or too low
If they get it right tell them and end the code
"""

# loop probably
# random num
# check for int input
# if else to see if guess is high or low
# user input
# make sure something ends the loop
# while loop

import random
secret_num = random.randint(1, 100)
not_guessed = True

while not_guessed:
    guess = int(input("Enter your guess: "))
    if guess > secret_num:
        print("too high")
    elif guess < secret_num:
        print("too low")
    else:
        print("you guessed it!")
        not_guessed = False



