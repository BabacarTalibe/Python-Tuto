# Tuple : ordonnées, immuables, indexées, non modifiables
# Tuples are defined using parentheses and can contain mixed data types.
# They are immutable, meaning once created, their elements cannot be changed.
x = ("dada", 22, "dakar", 45.5, True, 22)
y = ("baba", 25, "paris", 50.5, False, 25)
p = ("hello",) * 5
q = (12, 34, 56)
z = x + y + p  # Concatenate tuples
print(x)
print(x[0])  # Access the first element
print(z)  # Concatenate tuples
print(max(q))  # Get the maximum value in tuple q
print(min(q))