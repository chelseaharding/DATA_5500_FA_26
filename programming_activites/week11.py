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

""" 
Programming activity 3 (Not required for the online section Fall 2026)

Create a class called Time with an __init__ method that accepts an hour, minute, and second. Add getter and setter methods called time. Its getter should return the three values as a tuple, such as (14, 30, 0). Its setter should accept a tuple and update all three values. Test your class by creating a Time object, printing time, assigning a new tuple to time, and printing it again.
"""
# time class
class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    @property
    def get_time(self):
        return str(self._hour)+":"+str(self._minute)+":"+str(self._second)

    # @time.setter
    def set_time(self, hour, minute, second):
        if hour < 0 or hour > 23:
            raise ValueError("Hour must be between 0 and 23")
        self._hour = hour

        if minute < 0 or minute > 59:
            raise ValueError("Minute must be between 0 and 59")
        self._minute = minute

        if second < 0 or second > 59:
            raise ValueError("Second must be between 0 and 59")
        self._second = second

time1 = Time(10, 15, 2)
print(time1.get_time())
""" 
Programming activity 4 (Not required for the online section Fall 2026)

Create a class called Invoice that stores an item’s description, quantity, and price per item. Use an __init__ method to set these values, and make the quantity a private attribute. Add a getter method to view the quantity and a setter method to update it. If the new quantity is negative, print "Invalid quantity" and leave it unchanged. Add a method that calculates the total cost by multiplying the quantity by the price. Test your class by creating an invoice, changing its quantity, and printing the item’s description and total cost.

"""