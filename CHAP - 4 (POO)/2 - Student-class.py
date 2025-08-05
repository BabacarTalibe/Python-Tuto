class Student:
    #init method is called when an object is created from a class
    #it allows the class to initialize the attributes of a class
    def __init__(self):
        self.name = 'Cheikh'
        self.age = 20
        self.marks=95
        print("Init Method called: Student object created with default values.")
    #Instance method to display the attributes of the Student class
    #self refers to the instance of the class
    def display(self):
        print(f"Name - {self.name} \nAge - {self.age} \nMarks - {self.marks}")

s1 = Student()
print(id(s1))
print(s1.name)  # Accessing the name attribute

s1.name = 'Babacar'  # Update the name attribute
s1.age = 30
s1.display()  # Displays the attributes of the Student object    

print("---------------------------------------------------------------")
#Creating another instance of the Student class
#This will call the __init__ method again, creating a new object with default values
s2 = Student()   
print(id(s2))
s2.display() 