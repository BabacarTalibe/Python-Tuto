#Multiple constructors in Python
#Python does not support method overloading like some other languages, 
#but we can achieve similar functionality using default arguments or variable-length arguments.
class Student:
    # init method is called when an object is created from a class
    # it allows the class to initialize the attributes of a class
    def __init__(self, name):
        print("1st __in  it method called")
        self.name = name
    def __init__(self, name, age):
        print("2nd __init__ method called")
        self.name = name
        self.age = age
    def __init__(self, name, age, **marks):
        print("3rd __init__ method called")
        self.name = name
        self.age  = age
        self.marks = marks
        print("Init Method called: Student object created with default values.")
    
    def display(self):
        if hasattr(self.name) and hasattr(self.age) and hasattr(self.marks):
            print(f"Name - {self.name} \nAge - {self.age} \nMarks - {self.marks}")
        elif hasattr(self.name) and hasattr(self.age):
            print(f"Name - {self.name} \nAge - {self.age}")
        elif hasattr(self.name):
            print(f"Name - {self.name}")
        else:
            print("No attributes to display.")
        
s1 = Student("babacar", 12, Science = 18.5, Math = 20.5, English = 19.5)

print("---------------------------------------------------------------")