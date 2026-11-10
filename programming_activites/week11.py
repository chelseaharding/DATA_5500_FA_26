"""
Programming activity 1

Create a class called Square Use an __init__ method to store the square’s side length. 
Add three calculations for perimeter, area, and the diagonal of the square. 
"""
import math

class Square:
    def __init__(self, side):
        self.side = side

    def perimiter(self):
        return self.side * 4

    def area(self):
        return self.side ** 2

    def diagonal(self):
        return self.side * math.sqrt(2)

square1 = Square(5)
print(square1.perimiter())
print(square1.area())
print(square1.diagonal())