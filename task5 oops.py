# take student data from user and display it
class Student:
    def __init__(self):
        self.name=""
        self.age=""
        self.clas=""
        self.div=""
        self.marks=""
        
    def add_data(self):
        self.name=input("enter name - ")
        self.age=int(input("enter age - "))
        self.clas=input("enter class - ")
        self.div=input("enter division - ")
        self.marks=input("enter marks - ")
        
    def show(self):
        print("____Student data____")
        print(f"NAME= {self.name}")
        print(f"AGE= {self.age}")
        print(f"CLASS= {self.clas}")
        print(f"DIV= {self.div}")
        print(f"MARKS= {self.marks}")
        
s1=Student()
s1.add_data() 
s1.show()       