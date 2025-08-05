class Student:
    def __init__(self):
        self.name = 'Cheikh'
        self.age = 20
        self.marks=95
    
    def display(self):
        print(f"Name - {self.name} \nAge - {self.age} \nMarks - {self.marks}")

s1 = Student()
s1.name = 'Babacar'  # Update the name attribute
s1.age = 30
s1.display()  # Displays the attributes of the Student object    


s2 = Student()   
s2.display() 