"""Define a Employee class with attributes role, department & salary. This class also has
showDetails() method.
Create an Engineer class that inherits properties from Employee & has aditional
attributes:name & age."""
class Employee:
    def __init__(self,role,dept,salary):
        self.role=role
        self.dept=dept 
        self.salary=salary
    def show_details(self):
        print("role=",self.role)
        print("dept=",self.dept)
        print("salary=",self.salary)
        
class Engineer(Employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("Engineer","IT","80000")

e1=Employee("accountant","finance","60000")
e1.show_details()

engg1=Engineer("elon musk",0)
engg1.show_details()