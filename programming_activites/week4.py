"""
Programming Activity 1

Write a program which can adds up the numbers in the series:
1/2 + 1/4 + 1/8 + 1/16 + 1/32 for 1000 iterations.
create a variable for the denominator
for loop for 1000 iterations
start for loop at 1, go to 1000
variable to track the sum
What number is the result?
"""

# denom = 2
# sum   = 0
# for i in range(1, 54+1):
#     sum += 1/denom
#     denom *= 2
#     print("Sum:", sum)

"""
Programming Activity 2

Create a list called "colors" and assign it with your 3 favorite colors, as strings. Write a for loop to iterate through the list and print the values 
in the list.
- Create the list and assign the values.
- For loop through the values in the list.
"""

"""
Programming Activity 3

Update the loop in activity 2 to not only iterate through the colors in the list, but also iterate through each character in each string.
- Nested for loop, to iterate through the characters in each color.
"""

"""
Programming Activity 4

Create a list that stores 10 random integers. Start with an empty list, then use the append(), and the random.randint() function to generate the list.
- Create an empty list.
- For loop 10 times and append a random number each time.
"""
import random

nums = []

for i in range(10):
    nums.append(random.randint(1, 100))

print("nums:", nums)

"""
Programming Activity 5

Using the list you generated in programming activity 4, extend your program to check if there are 2 even numbers in a row. If there are two even numbers in a row, print the numbers.
- There's a few ways to approach this, you could:
      1. use the index operator: lst[count] and lst[count+1]
      2. use slice operator: lst[count:count+2]
      3. use separate to store previous or next, and check if those are even
- No matter which way you chose you need to:
- Each iteration in the loop check if the current number and next number are both even.
"""
i = 0
for num in nums:
    if i > 0:
        print(nums[i])
        print(nums[i-1])
        if nums[i] % 2 == 0 and nums[i-1] % 2 == 0:
            print("both", nums[i], "and", nums[i-1], "are even")
    i += 1

"""
Programming Activity 6

Write a Python program that creates a list of all even numbers from 2 to 100 using list comprehension.
"""

"""
Programming Activity 7

Write a Python program that takes a list of strings as input, where some strings might have leading or trailing spaces. Use list comprehension to remove these spaces from each string in the list.
"""

"""
Programming Activity 8

Write a program which determines whether a child can sit in the front seat  of a car, using the following logic:
- if a child is 12 years old or older, they can sit in the front, regardless of weight.
- if a child is 11 years old, and over 90 pounds, they can sit in the front seat.
- if a child is under 11 years old, and over 100 pounds, they can sit in the front seat
- if a child does meet the criteria above they cannot sit in the front seat.
Your program will ask the user for a child's age and weight. Use Boolean variables to store the results of the criteria above. Use if statements and the Boolean variables created above to print a message to the user whether or not the child may sit in the front seat.
"""

# age = int(input("Enter age: "))
# weight = int(input("Enter weight: "))

# criteria_1 = age >= 12
# criteria_2 = age == 11 and weight >= 90
# criteria_3 = age < 11 and weight >= 100

# if criteria_1:
#     print("You can sit in the front seat!")
# elif criteria_2:
#     print("You can sit in the front seat!")
# elif criteria_3:
#     print("You can sit in the front seat!")
# else:
#     print("NO!")

# if criteria_1 or criteria_2 or criteria_3:
#     print("You can sit in the front seat!")
# else:
#     print("nah...")