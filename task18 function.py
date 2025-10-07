def rectangle(l,b):    
    ar=l*b
    peri=2*(l+b)
    print("area of rectangle is=",ar)
    print("perimeter of rectangle is =",peri)
def square(s):
    ar=s*s
    peri=4*s
    print("area of square is=",ar)
    print("perimeter of square is =",peri)
    
def circle(r):
    ar=3.14*r**2
    peri=2*3.14*r
    print("area of circle is=",ar)
    print("perimeter of circle is =",peri)
    
def triangle(a, b, c, h):
    ar = 0.5 * b * h
    peri = a + b + c
    print("area of triangle is =", ar)
    print("perimeter of triangle is =", peri)    




def main():
    print("===== SHAPES =====")
    print("1. rectangle")
    print("2. square")
    print("3. circle")
    print("4. triangle")
    print("5. Exit")

    while True:
        ch = int(input("\nEnter your choice (1-5) = "))

        if ch == 1:
            rectangle(12,2)   
        elif ch == 2:
            square(5)
        elif ch == 3:
            circle(12)
        elif ch == 4:
            triangle(2,3,4,5)
        elif ch == 5:
            print(" Exiting... Goodbye!")
            break
        else:
            print(" Invalid choice! Please enter between 1–5.")      
main()