#Agregation exemple
#Agreagation is a relationship where one class contains a reference to another class, but both can exist independently.

class Salary:
    def __init__(self, pay, reward ):
        self.pay = pay
        self.reward = reward
        
    def annual_salary(self):
        return self.pay * 12 + self.reward
class Employee:
    def __init__(self, name,position, salary):
        self.name = name
        self.position = position
        self.final_salary = salary

    # Method to get the final salary

    def get_final_salary(self):
        return self.final_salary.annual_salary() 
    
    # Method to display employee details

    def display(self):
        print(f"Name: {self.name}, Position: {self.position}, Annual Salary: {self.get_final_salary()}")
        
salary = Salary(5000, 2000)
      
# Example usage
emp1 = Employee("Alice", "Developer", salary)

emp1.get_final_salary()
emp1.display()
