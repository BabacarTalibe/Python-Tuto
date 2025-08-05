from polygone import Polygon
from shape import Shape
class Square(Polygon, Shape): # Inheriting from Polygon
    def area(self):
        return self.get_width() * self.get_height()
