#negative indexing
#negative indexing allows you to access elements from the end of a list or string
#the last element is -1, the second last is -2, and so on

x = [100, 101, 102, 103, 104, 105, 106]
y = (60, 10, 70, 100, 40, 50, 90, 80)
z = "Babacar"

print(x[0:3])  # Access elements from index 0 to 2
print(x[4:])  # Access elements from index 0 to 2
print(x[:])  # Access all elements
print(x[::-2])  # Access elements in reverse order
print(x[::2])
print(x[-3::])  # Access elements from the end


