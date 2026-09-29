
"""
Programming Activity 1

1. Download one year worth of stock data from yahoo finance. The instructions to do this are in the HW3 description.
2. After you have one year worth of stock data, use a for loop to iterate through the data, and calculate the average for the entire data set.
3. After you have calculated the average for the entire data set, see if you can calculate the average for the first 5 days only.  
(you will need this logic for your homework).
"""

"""
Programming Activity 1.2 
This activity is a continuation from the last one and is meant to help you with your homework.
Write a Python program to read in the stock prices from a file, into a list.
Create a list of floats from the list of strings you read in, from step 2.
Calculate the average of the first 4 days in your list.
Calculate the average of the last 4 days in your list.
In a for loop, calculate a 4 day moving average for the floats in the list.
Add logic in the for loop to implement a simple moving average trading strategy.
Display the profit from the strategy, after the for loop has finished.
"""

"""
Programming Activity 2

Write a program, and have the user enter their name and their favorite color, as two separate variables. Write the sentence to a file using the with command "<name>'s favorite color is <color>"
- get two variables from user
- use the with command to open the file
- use the write function to write to the file
"""
name = input("Enter your name: ")
color = input("Enter your fav color: ")

with open("/workspaces/DATA_5500_FA_26/programming_activites/prog_act_5.txt", "w") as info_file:
    info_file.write(name + "'s favorite color is " + color)