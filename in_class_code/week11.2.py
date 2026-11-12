"""
Accessing class attributes :)
"""

class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

# problem with allowing direct access to class attributes
account1 = Account("Big Blue", 18.88)
print(account1.balance)
account2 = Account("Thistle", -1000)
print(account2.balance)

# time class
class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    #getters and setters
    # property is the getter
    @property
    def hour(self):
        return self._hour

    # hour setter is the setter
    @hour.setter #wrapper
    def hour(self, hour):
        # set the range of acceptable hours
        if hour < 0 or hour > 23:
            raise ValueError("Hour must be between 0 and 23")
        self._hour = hour

    #minutes
    @property
    def minute(self):
        return self._minute

    @minute.setter
    def minute(self, minute):
        if minute < 0 or minute > 59:
            raise ValueError("Minute must be between 0 and 59")
        self._minute = minute


time1 = Time(12, 20, 4)
print(time1.hour)
print(time1.minute)
# time2 = Time(100, 100, 100)

"""
How to simulate private data with classes
"""

class PrivateClass:
    def __init__(self):
        self.public_data = "I am public! :)"
        self.__private_data = "I am private :("
        self._semi_private_data = "this is sort of private"

    def get_private_data_safely(self):
        return self.__private_data


privateClass1 = PrivateClass()
print(privateClass1.public_data)
print(privateClass1._semi_private_data)
print(privateClass1.get_private_data_safely())
    