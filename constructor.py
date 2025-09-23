class Student():
    college_name="ABC"     #CLASS ATTRIBUTES
    #default constructor
    """def __init__(self,):
        pass"""
    #parametrized constructor
    def __init__(self,fullname,marks): #self ic compoulsary self==object
        print(self)
        self.name=fullname   #OBJECT ATTRIBUTES
        self.marks=marks
        print("adding new student to db")
s1=Student("rohan",99)
print(s1.name,s1.marks)
s2=Student("arjun",88)
print(s2.name,s2.marks,)
print(s2.college_name)