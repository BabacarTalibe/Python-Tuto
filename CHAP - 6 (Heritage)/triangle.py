from polygone import Polygon
from shape import Shape
class Triangle(Polygon, Shape): # Inheriting from Polygon
    def area(self):
        return self.get_width() * self.get_height() * 1/2
    