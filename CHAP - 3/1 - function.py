# def sum_f(a,b):
#     if type(a) == type(b):
#         return a + b
#     else:
#         return "Error: Both arguments must be of the same type"
# x = 10
# y = 50

# result = sum_f(x, y)
# print(result)  # Prints the result of the sum_r function

def shop(item, price, quantity):
    if type(item) == str and type(price) == int and type(quantity) == int:
        total_price = price * quantity
        return f"{item} costs {total_price} dollars"
    else:
        return "Error: Invalid input types"

print(shop(price=200, item="apple", quantity=3))  # Correct usage
print("---------------------------------------------------------------")
#Passing a tuple as an argument *marks
def std(name, clas, *marks):
    print("name", name)
    print("Class", clas)
    
    print(marks)
    for mark in marks:
        print("Marks", mark)  
    
std("Alice", "10th Grade", 85, 90, 78)  # Example usage with variable number of marks
#Passing a dictionary as an argument **marks
print("---------------------------------------------------------------")

def std(name, clas, **marks):
    print("name", name)
    print("Class", clas)
    print(marks)
    
    for x,y in marks.items():
        print(x, "mark is", y)  
    
    
std("Alice", "10th Grade", Math=85, English=90, Physics=78)  # Example usage with variable number of marks
print("---------------------------------------------------------------")