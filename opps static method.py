class Student():
    def __init__(self,fullname,marks): 
        print(self)
        self.name=fullname   #OBJECT ATTRIBUTES  
        self.marks=marks
    @staticmethod     #DECORATOR
    def hello():
        print("hello")
    def get_marks(self):
        return self.marks
        
s1=Student("rohan",99)
s1.hello()
print(s1.get_marks())
        
        