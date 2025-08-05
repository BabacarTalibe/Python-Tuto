from square import Square as sq
from triangle import Triangle as tq

s1 = sq()
s1.set_value(5, 5)
s1.set_color("red")
print(f"Area of square: {s1.area()}, , Color of Square {s1.get_color()}")  # Output: Area of square: 25

print("---------------------------------------------------------------")

t1 = tq()
t1.set_color("blue")
t1.set_value(5, 10)
print(f"Area of triangle: {t1.area()}, Color of triangle {t1.get_color()}")  # Output: Area of triangle: 25.0