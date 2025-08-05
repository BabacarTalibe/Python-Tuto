#list are mutable
#list are ordered
#list can contain different data types
#list can contain duplicate items
x = ["dada", 22, "dakar", 45.5, True, 22]
print(x[0])  # Access the first element
len_x =  len(x)  # Get the length of the list
print(len_x)  # Print the length of the list
x.remove("dada")  # Remove the first occurrence of "dada"
x.insert(0, "new_item")  # Insert a new item at index 2
print(x)  # Print the updated list
x.pop()  # Remove the last item from the list
x.append(70)  # Append a new item to the end of the list
x.count(22)  # Count occurrences of 22 in the list
print(x)  # Print the updated list
del(x)  # Delete the entire list