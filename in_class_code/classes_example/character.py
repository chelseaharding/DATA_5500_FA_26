"""
OOP
"""

"""
Reasons to like :)
1 - Modularity
2 - Reusability
3 - Maintenence - debugging - errors
4 - Model real world things
5 - Encapsulation
"""

class Character:
    # class attribute
    game_title = "Mario Kart"

    # initalize function
    def __init__(self, name, car, size, speed, catchphrase, is_evil):
        self.name = name
        self.car = car
        self.size = size
        self.speed = speed
        self.catchphrase = catchphrase
        self.is_evil = is_evil
        self.items = []

    # method to pick up an item
    def pick_up_item(self, item):
        if len(self.items) <= 1:
            self.items.append(item)
            print("You picked up", item)

    # method to use an item
    def use_item(self):
        if len(self.items) >= 1:
            print("You used", self.items[0])
            self.items.pop(0)

    def __repr__(self):
        return self.name + ": " + self.catchphrase


# mario = Character("Mario", "Standard Bike", "Medium", 5, "It's a me! Mario!", False)

# print(type(mario))
# print(mario)
# mario.pick_up_item("banana")
# mario.pick_up_item("star power")
# mario.pick_up_item("bullet bill")

# print(mario.items)

# mario.use_item()



