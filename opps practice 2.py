class Employee:
    def __init__(self):
        self.emp_id=101

        self.ename='Harri'
        
    def Display(self):
        print(f"emp id is {self.emp_id} and name is {self.ename}")
        
obj=Employee()
obj.Display()

class Employee:
    def __init__(self,salary,desigation):
        self.salary=salary
        self.designation=desigation
        
    def Show(self):
        print(f"saalry {self.salary} and designaton is {self.designation}")
        
        
emp=Employee(12000,'Accoutant')
emp.Show()
        
        
        
#inheritance
class Animal:
    def __init__(self):
        self.name='Domestic Animal'
        self.color='black'
        
    def Show(self):
        print(f"name is {self.name} and color is {self.color}")
        
        
class Birds(Animal):
    def Deatils(self):
        Animal.Show(self)
        print("birds can fly")
        
anim=Birds()
anim.Deatils()


#multiple
class Father:
    def __init__(self):
        pass
    def Display(self):
        self.fname="xyz"
        print(f"father name is {self.fname}")
        
class Mother:
    def __init__(self):
        pass
    def Display(self):
        self.mname="pqr"
        print(f"mother  name is {self.mname}")
        
class Child(Father,Mother):
    def __init__(self):
        pass
    def Display(self):
        Father.Display(self)
        Mother.Display(self)
        self.cname="qwe"
        print(f"child  name is {self.cname}")

c=Child()
c.Display()

# multilevel
class Grandather:
    def __init__(self):
        pass
    def Display(self):
        self.gname="xyz"
        print(f"grandfather name is {self.gname}")
        
class Father(Grandather):
    def __init__(self):
        pass
    def Display(self):
        Grandather.Display(self)
        self.fname="pqr"
        print(f"father  name is {self.fname}")
        
class Child(Father):
    def __init__(self):
        pass
    def Display(self):
        Father.Display(self)
        self.cname="qwe"
        print(f"child  name is {self.cname}")

c=Child()
c.Display()

# Hierarchical
class Father():
    def __init__(self):
        pass
    def Display(self):
        
        self.fname="pqr"
        print(f"father  name is {self.fname}")
        
class Child1(Father):
    def __init__(self):
        pass
    def Display(self):
        Father.Display(self)
        self.cname1="wdf"
        print(f"1st child  name is {self.cname1}")
        
class Child2(Father):
    def __init__(self):
        pass
    def Display(self):
        Father.Display(self)
        self.cname2="asd"
        print(f"2ND child  name is {self.cname2}")
        
class Child3(Father):
    def __init__(self):
        pass
    def Display(self):
        Father.Display(self)
        self.cname3="qwe"
        print(f"3rd child  name is {self.cname3}")

c=Child1()
c.Display()
d=Child2()
d.Display()
r=Child1()
r.Display()