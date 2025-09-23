class Student():
    def __init__(self,fullname,marks): 
        print(self)
        self.name=fullname   #OBJECT ATTRIBUTES  
        self.marks=marks
    def hello(self):
        print("hello",self.name)
    def get_marks(self):
        return self.marks
        
s1=Student("rohan",99)
s1.hello()
print(s1.get_marks())
        
        