#CREATE STUDENT CLAS THAT TAKES NAME &MARKS OF 3 SUB AS ARGUMENTS TI CONSTRUCTOR 
#THEN CREATE A METHOD TO PRINT THE AVERAGE

class Student():
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        
    def cal_avg(self):
        sum=0
        for val in self.marks:
            sum+=val
        print("hii", self.name,"your avg score is :",sum/3)
s1=Student("rohan",[99,88,99])
s1.cal_avg()