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

"""
Programming Activity 5

Write a program which asks the user their age, then using a while loop displays the year they were born, using the following rules:
 - continue the loop while age is greater than 1
 - print each time "you were alive in year: " current_year
 - decrease age and current_year by one each time
 - add an else saying "you were born in year: " current_year
"""
age = int(input("How old are you: "))
current_year = 2026

while age >= 1:
    print("You were alive in", current_year)
    age -= 1
    current_year -= 1
else:
    print("you were born in", current_year)

"""
Programming Activity 6

Write a program that prints all the multiples of 5, from 5 to 95 using a for loop. 
"""
for i in range(5, 96, 5):
    print("i:", i)

"""
Programming Activity 7

Write a program that prints all the multiples of 5, from 5 to 95 using a while loop.
"""
num = 0
while num < 96:
    print("num:", num)
    num += 5

"""
Programming Activity 8

Write a program which can tell if a 3 digit number is a palindrome. 
 - Create a variable, which stores user input. Prompt the user to enter a 3 digit number. 
 - Convert the user input into a integer (int). To get the first digit alone, floor division by 100. 
 - To get the 3rd digit alone, modulus by 10. 
 - Check if the first digit and 3rd digit are the same. 
 - If they are the same print("palindrome!!!!"). 
 - Else print("not palindrome!")
"""

palindrome_maybe = int(input("Enter a 3 digit number: "))

first_num = palindrome_maybe // 100
third_num = palindrome_maybe % 10

if first_num == third_num:
    print("your number is a palindrome")
else:
    print("your number is not a palindrome")