# x = int(input("Number 1"))
# y = int(input("Number x"))
# try:
#     res = x / y
# except TypeError as e: 
#     print("Inside TypeError",e)
# except ZerodivisionError as e:
#     print("Inside ZeroDivisionError",e)

# print(f"resultat : {res}")

x = int(input("Number 1"))
y = int(input("Number x"))
try:
    res = x / y
except Exception as e: #class de base
    print(type(e))
else: # executed when no exception tiggered
    print(Inside else)
finally: #executed any time
    print(inside finally) #data management



print("------------------New Line--------------------")
print(f"resultat : {res}")