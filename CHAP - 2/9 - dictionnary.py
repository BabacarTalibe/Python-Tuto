#dictionary are mutable data types in Python
# They are unordered collections of key-value pairs.
# Keys must be unique and immutable, while values can be of any data type.
# Dictionaries are defined using curly braces {}.
class_room = {"name": "Alice", "age": 20, "grade": "A", "(x,y)": (1,2)}

print(class_room.items())  # Returns dict_items([('name', 'Alice'), ('age', 20), ('grade', 'A')])
print(class_room.keys())   # Returns dict_keys(['name', 'age', 'grade'])
print(class_room.values()) # Returns dict_values(['Alice', 20, 'A'])

class_room["age"] = 18  # Update the age
print(class_room["age"])  # Prints the updated age
class_room.pop("(x,y)")
class_room.update({"name":"Alice"})  # Update the name to "Bob"
print(class_room)  # Prints the updated dictionary
for x,y in class_room.items():
    print(f"{x} : {y}")  # Prints each key-value pair in the dictionary
    
del(class_room)  # Deletes the entire dictionary
print("Class room dictionary deleted.")  # Confirmation message after deletion