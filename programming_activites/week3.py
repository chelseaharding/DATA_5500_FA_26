"""
Programming Activity 1

 1. make a variable called apple_price (set it to whatever you want)
 2. make a variable called number_purchased (set it to whatever you want)
 3. make a variable called tax and set it equal to 1.07
 4. make a variable, total_bill and calculate it by: total_bill = apple_price * number_purchased * tax
 5. print clearly and cleanly how many apples were purchased and the total_bill
 6. add a check before the final print statement to see if total_bill is equal to 0.  If so, print a message to the user to check their inputs.
"""

apple_price = 2.60
number_purchased = 3
tax = 1.07
total_bill = apple_price * number_purchased * tax
print("You bought", number_purchased, "apples for", apple_price, "a piece. Your total bill is", total_bill)

"""
Programming Activity 2

Write a program that asks the user how old they are, and what age they would like to live to. Calculate how long they have left to live (approximately), and then print a friendly message telling the user how long they have to 
live.
"""
# current_age = int(input("How old are you: "))
# desired_age = int(input("How old would you like to be when you die: "))

# print("You have", desired_age-current_age, "years left to live :)")

"""
Programming Activity 3

Write a program that gets a user's score in this class, as a percentage i.e. 90 or 95. Write an if statement that checks to see if their score is equal to or greater than 93.  If so, print "Congratulations you got an A" else print "Congratulations, you still learned a ton!!!!"
"""


"""
Programming Activity 4

Write a program that asks the user the year they were born. Display a message telling the user what generation they belong to based on the following rules/years:
 - Gen Beta 2024
 - Gen Alpha 2013
 - Zoomer 1997
 - Millennial 1981
 - Gen X 1965
 - Baby Boomer 1946
"""

birth_year = int(input("What year were you born in: "))

if birth_year >= 2024:
    print("You are gen Beta")
elif birth_year >= 2013:
    print("You are gen Alpha")
elif birth_year >= 1997:
    print("You are gen Z")
elif birth_year >= 1981:
    print("You are Millennial")
elif birth_year >= 1965:
    print("You are gen X")
else:
    print("You are a baby boomer")