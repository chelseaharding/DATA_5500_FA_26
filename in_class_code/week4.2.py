"""
List stuff
"""

fav_colors = ["Aggie Blue", "Fighting White", "Sage"]
for color in fav_colors:
    for letter in color:
        print("letter:", letter)

# append
fav_colors.append("Purple")

# insert
fav_colors.insert(1, "Mustard Yellow")
print(fav_colors)

# indexing
i = 0
for color in fav_colors:
    print("color:", color)
    # print("fav_colors[i]:", fav_colors[i+1])
    i += 1

# palindrome - how to check using list slicing
word = "racecar"

# [::-1] - reverse a list
letters = []
for letter in word:
    letters.append(letter)
print(letters)

if letters == letters[::-1]:
    print("You found a palindrome :)")

# list comprehension 
words = ["John", "python", "civic", "tacocat", "goat", "cheese", "noon", "hannah", "Kayak"]

pals = [word for word in words if word == word[::-1]]

print("pals:", pals)

# anagrams
word1 = "thonpy"
word2 = "python"

if sorted(word1) == sorted(word2):
    print("yes")
else:
    print("not the same letters")