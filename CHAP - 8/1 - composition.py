#composition : relationship has-a
# In this example, we demonstrate the concept of composition in Python by creating an Employee class that has a Salary class.
# The Employee class uses the Salary class to calculate the annual salary based on monthly pay and rewards.
class Salary:
    def __init__(self, pay, reward ):
        self.pay = pay
        self.reward = reward
        
    def annual_salary(self):
        return self.pay * 12 + self.reward
class Employee:
    def __init__(self, name,position, pay, reward):
        self.name = name
        self.position = position
        self.final_salary = Salary(pay, reward) # composition

    # Method to get the final salary

    def get_final_salary(self):
        return self.final_salary.annual_salary() 
    
    # Method to display employee details

    def display(self):
        print(f"Name: {self.name}, Position: {self.position}, Annual Salary: {self.get_final_salary()}")
        
        
# Example usage
emp1 = Employee("Alice", "Developer", 5000, 2000)

emp1.get_final_salary()
emp1.display()
emp2 = Employee("Bob", "Manager", 7000, 3000)