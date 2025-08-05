# name = input("Enter your name: ").strip().lower()
# age= int(input("Enter your age: ").strip())
# marks = float(input("Enter your marks: ").strip())

class Student:
    # init method is called when an object is created from a class
    # it allows the class to initialize the attributes of a class
    def __init__(self, name, age, **marks):
        self.name = name
        self.age  = age
        self.marks = marks
        print("Init Method called: Student object created with default values.")
    
    def display(self):
        print(f"Name - {self.name} \nAge - {self.age} \nMarks - {self.marks}")
        
s1 = Student("babacar", 12, Science = 18.5, Math = 20.5, English = 19.5)
s1.display()  # Displays the attributes of the Student object

print("---------------------------------------------------------------")