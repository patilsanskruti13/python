class Shape:
    def area(self):
        pass
    def perimeter(self):
        pass
class Rectangle(Shape):
    def __init__(self):
        self.leng=float(input("enter length for rectangle="))
        self.breadth=float(input("enter breadth for rectangle="))
    def area(self):
        print("Area of rectangle is :" ,self.leng*self.breadth)
    def perimeter(self):
        print("Perimeter of rectangle  is :", 2*(self.leng+self.breadth))   
        
class Square(Shape):
    def __init__(self):
        self.leng=float(input("enter length for square="))
    def area(self):
        print("Area of square is :" ,self.leng*self.leng)
    def perimeter(self):
        print("Perimeter of square  is :", 4*self.leng)    
    
class Circle(Shape):
    def __init__(self):
        self.rad=float(input("enter radius for circle="))
    def area(self):
        print("Area of circle is :" ,3.14*self.rad**2)
    def perimeter(self):
        print("Perimeter is :", 2*3.14*self.rad)     
    
    
# ---- Choice-driven menu with exit ----
while True:
    print("\nChoose a shape:")
    print("1. Rectangle")
    print("2. Square")
    print("3. Circle")
    print("4. Exit")

    choice = int(input("Enter your choice (1/2/3/4): "))

    if choice == 1:
        rect = Rectangle()
        rect.area()
        rect.perimeter()
    elif choice == 2:
        sq = Square()
        sq.area()
        sq.perimeter()
    elif choice == 3:
        cr = Circle()
        cr.area()
        cr.perimeter()
    elif choice == 4:
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")
