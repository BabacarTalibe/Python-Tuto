#Encapsulation in Python
#Encapsulation is a fundamental concept in object-oriented programming that restricts direct access to an object's attributes and methods.
#In Python, encapsulation is achieved through the use of private and public attributes.
class Speed:
    def __init__(self):
        self.speed = 10
        self.__new_speed = 15  # Private attribute (__), not accessible outside the class
    def get_new_speed(self):
        return self.__new_speed  # Method to access the private attribute

    def set_new_speed(self, speed):
        if speed > 0:
            self.__new_speed = speed
s1 = Speed()
s1.speed = 20
print(s1.speed)  # Accessing the speed attribute
s1.set_new_speed(25) # Attempting to modify the private attribute (not recommended)
print(f"the new_speed value is {s1.get_new_speed()}")  # Accessing the speed attribute
