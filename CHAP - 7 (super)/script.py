class Parent1:
    def __init__(self, name):
        print("Parent __init__ ", name)
        
class Parent2:
    def __init__(self, name):
        print("Parent __init__ ", name)

class child(Parent1, Parent2):
    
    def __init__(self):
        print("Child __init__ ")
        super().__init__("Joseph")
        Parent2.__init__(self, "John")

child_obj = child()
print(child.mro())  # Display the method resolution order
