"""
Functions!
"""

# reuseablilty
# Simpler
# Customization
# Readable
# Efficient 
# Testing
# Code Organization
# Modularity

# Functions need 4 things:
# 1 - Name/Definition
# 2 - Arguments (or no arguments)
# 3 - Main Body of Code
# 4 - Return (or no return)



# temperature converter f to c
def f_to_c(ftemp):  # name/def - argument(s)
    ctemp = (ftemp - 32) * 5/9 # main body of code
    # print(ctemp)
    return ctemp

temps = [32, 0, 78]
ctemps = []
for temp in temps:
    ctemps.append(f_to_c(temp))

print("ctemps:", ctemps)


# write c_to_f
def c_to_f(ctemp):
    ftemp = (ctemp * 9/5) + 32
    return ftemp
    print(ftemp) #this line will never be run