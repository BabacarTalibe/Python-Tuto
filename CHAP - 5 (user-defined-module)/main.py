# from mymodule import mymath
import mymodule.mymath as mymath

sum = mymath.add(5, 3)
mult = mymath.multiply(4, 2)
print(f"The result of multiplication is: {mult}")
print(f"The result of addition is: {sum}")