"""
Programming Activity 1

Write a function named "welcome_fctn" which takes one argument, called "name".  Inside the function, 
print to the console "Welcome " name.
- Use the def command to define a function "welcome_fctn"
- Add a parameter list with one variable "name", i.e. (name)
- Print "Welcome " name in the function body.
- We don't need a return statement here, but keep in mind python does return nothing.
- Call the function, welcome_fctn(<your_name>)
"""
def welcome_function(name):
    print("Welcome", name)

welcome_function("Cloud")
"""
Programming Activity 2

Update the function in activity one, and create a new string variable in the function called, welcome_message. The variable welcome_message should be 
assigned the value "Welcome " name. The same value printed in activity 1, but here you save it as a variable. Return the variable welcome_message.
- Assuming your function in programming activity 1 works, you will need to:
- Create a variable to store "Welcome " + name
- Return the value welcome_message
- There are a couple ways to test this. you could
         1. Print(welcome_fctn("Bob"))
         2. Create a variable to store what is returned by the function then print that
"""
def welcome_2(name):
    welcome_message = "Welcome " + name
    return welcome_message

print(welcome_2("Cloud"))

"""
Programming Activity 3

Update the function in activity one to have 3 variables: name (string),  age (int), favorite_color (string).  Create a new variable called welcome_message and assign it to the value "Welcome <name>, you are <age> years old, and <favorite_color> is your favorite color".  Return the variable welcome_message.
- Add two variables to your parameter list
- Concatenate those two variables in your welcome_message
- Return welcome_message just like you did in activity 2
- To test this, call welcome_fctn with 3 arguments
"""
name = input("Name: ")
age = int(input("Age: "))
color = input("Color: ")

def welcome_3(name, age, favorite_color):
    welcome_message = "Welcome " + name + ". You are " + str(age) + " years old, and your favorite color is " + favorite_color + "."
    return welcome_message

print(welcome_3(name, age, color))