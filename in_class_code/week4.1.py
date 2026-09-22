# sentinal values

# avg numbers until the user says to stop

total = 0
count = 0

while True:
    num = int(input("Enter a number. Enter -1 to stop: "))
    if num == -1:
        break
    total += num
    count += 1
    print("Avg:", total/count)

# nested statements
"""
Suppose you have a multiplication table that is N by N. Write code to find how many times a target number appears in the table

For example: given N = 6, X = 12 you should output 4
             given N = 4, X = 12 you should output 2

"""

# - nested statements (loops?)
# - range for N
# - loop over the range until it hits N

N = 8
X = 16

count = 0

for i in range(1, N+1):
    # print("i:", i)
    for j in range(1, N+1):
        # print("j:", j)
        print("i x j:", i*j)
        if i*j == X:
            count += 1

print("we found the target number", count, "times")

# boolean operators
is_raining = True # true

if is_raining:
    print("bring an umbrella")

age = 12+18
print(age)

age = 11
can_vote = age >= 18 # false

random_variable = can_vote and is_raining