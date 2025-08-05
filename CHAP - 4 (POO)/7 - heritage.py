class Polygon:
    __width = None
    __height = None
    def set_value(self, width, height):
        self.__width = width
        self.__height = height
    def get_width(self):
        return self.__width
    def get_height(self):
        return self.__height

class Square(Polygon): # Inheriting from Polygon
    def area(self):
        return self.get_width() * self.get_height()

class Triangle(Polygon): # Inheriting from Polygon
    def area(self):
        return self.get_width() * self.get_height() * 1/2
    
s1 = Square()
s1.set_value(5, 5)
print(f"Area of square: {s1.area()}")  # Output: Area of square: 25

print("---------------------------------------------------------------")

t1 = Triangle()
t1.set_value(5, 10)
print(f"Area of triangle: {t1.area()}")  # Output: Area of triangle: 25.0