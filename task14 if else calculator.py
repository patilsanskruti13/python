print("** calcuator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")
while True:
    choice=int(input("Enter your choice(1-5)= "))
    
    if choice==1:
        a=float(input("enter 1st no.="))
        b=float(input("enter 2nd no.="))
        print("result", a+b)
        
    elif choice==2:
        a=float(input("enter 1st no.="))
        b=float(input("enter 2nd no.="))
        print("result", a-b)
        
    elif choice==3:
        a=float(input("enter 1st no.="))
        b=float(input("enter 2nd no.="))
        print("result", a*b)
    elif choice==4:    
        a=float(input("enter 1st no.="))
        b=float(input("enter 2nd no.="))
        if b==0:
            print("can't divide")
        else:    
            print("result", a/b)
    elif choice==5:    
        print("Exiting... Goodbye!")
        break

    else:
        print("Invalid choice! Please enter between 1–5.")