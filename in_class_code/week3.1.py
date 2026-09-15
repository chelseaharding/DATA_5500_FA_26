# input and dynamic types

x = 12
print(type(x))
x = "twelve"
print(type(x))
x = True
print(type(x))
x = x
print(type(x))

# fav_day_week = input("Please enter your favorite day of the week: ")
# print(type(fav_day_week))

# casting
# float()
# int()
# str()
# bool()
# eval()

# int(fav_day_week)

# x = eval(input("Enter anything: "))
# print(type(x))

# pseudocode

# given a list of numbers, count how many are above the average of all the numbers on the list

"""
Steps:
 - variable to hold the avg
 - sort the list, everything above avg is greater
 - run a for loop to compare avg to each number in list
 - establish a list of numbers
 - print out which numbers are greater
"""

# control statements - if else if elif ect

x = "Thursday"
if x == "Tuesday":
    print("Worst day of the week :(")
else:
    print("Thank goodness :|")


# grades
grade = int(input("Enter your grade in this class: "))

if grade >= 93:
    print("you have an A")
elif grade >= 90:
    print("you have an A-")
elif grade >= 80:
    print("you have a B")
elif grade >= 70:
    print("you have a C")
else:
    print("you fail this class :'(")


# multiple conditions can be true or false
USUscore = 89
UtahScore = 700
hadAGreatTime = True

if USUscore > UtahScore:
    print("Go aggies, we win")
else:
    print("I don't want to talk about it")
if hadAGreatTime:
    print("You had a great time regardless of the outcome of the game")