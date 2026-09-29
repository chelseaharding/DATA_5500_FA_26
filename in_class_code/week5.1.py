"""
Files
"""

# read mode
file = open("/workspaces/DATA_5500_FA_26/README.md")
print(file.readlines())
file.close()

# write mode
file2 = open("write_me.txt", "w")
file2.write("Today is a great day\n")
file2.write("Scaramouche, Scaramouche, will you do the Fandango?\n")
file2.close()

# append mode
file3 = open("/workspaces/DATA_5500_FA_26/write_me.txt", "a")
file3.write("Thunderbolt and lightning, very, very frightening me\n")
file3.write("(Galileo) Galileo, (Galileo) Galileo, Galileo Figaro")
file3.close()

# with open
states = ["Utah\n", "Texas\n", "Idaho\n", "Alberta\n", "California\n", "Vermont\n", "Wyoming\n"]
with open("/workspaces/DATA_5500_FA_26/in_class_code/tuesday.txt", "w") as file:
    file.writelines(states)

