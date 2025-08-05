class Exemple:
    def __init__(self):
        self.x = 10
        self.__y = 20   # Private attribute (__), not accessible outside the class
        self.__z = 100  # Another private attribute
    def __init(self, x, y, z):
        self.x = x
        self.__y = y
        self.__z = z
        print("Init Method called: Exemple object created with default values.")    
    def get_y(self):
        return self.__y  # Method to access the private attribute
    def set_y(self, value):
        if value > 0:
            self.__y = value
    def get_z(self):
        return self.__z
    def set_z(self, value):
        if value > 0:
            self.__z = value
    def public_method(self):
        print("This is a public method.")
        self.__private_method()  # Calling the private method within the class
    
    def __private_method(self):
        print("This is a private method.")
        print(f"\t\t\tAccessing private attribute __y: {self.__y}")
        print(f"\t\t\tAccessing private attribute __z: {self.__z}")


s = Exemple()
#s.__private_method()  # Attempting to call the private method (will raise an error)
s.public_method()  # Calling the public method
        