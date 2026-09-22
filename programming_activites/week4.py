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

denom = 2
sum   = 0
for i in range(1, 54+1):
    sum += 1/denom
    denom *= 2
    print("Sum:", sum)

"""
Programming Activity 8

Write a program which determines whether a child can sit in the front seat  of a car, using the following logic:
- if a child is 12 years old or older, they can sit in the front, regardless of weight.
- if a child is 11 years old, and over 90 pounds, they can sit in the front seat.
- if a child is under 11 years old, and over 100 pounds, they can sit in the front seat
- if a child does meet the criteria above they cannot sit in the front seat.
Your program will ask the user for a child's age and weight. Use Boolean variables to store the results of the criteria above. Use if statements and the Boolean variables created above to print a message to the user whether or not the child may sit in the front seat.
"""

age = int(input("Enter age: "))
weight = int(input("Enter weight: "))

criteria_1 = age >= 12
criteria_2 = age == 11 and weight >= 90
criteria_3 = age < 11 and weight >= 100

if criteria_1:
    print("You can sit in the front seat!")
elif criteria_2:
    print("You can sit in the front seat!")
elif criteria_3:
    print("You can sit in the front seat!")
else:
    print("NO!")

if criteria_1 or criteria_2 or criteria_3:
    print("You can sit in the front seat!")
else:
    print("nah...")