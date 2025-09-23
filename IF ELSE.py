a=10
b=20
c=20
if b==a:
    print("both are equal")
elif b>a:
    print("b is greater than a")
else:
    print("a is greater than b") 
    
print("A") if a > b else print("B")

if a>b and b>c:
    print("both condition are same")
else:
    print("different")
    
if a>b or b>=c:
    print("At least one of the conditions is True")
else:
    print("different")    
    
x=41
if x>20:
    print("x is greater than 20")
    if x>40:
        print("and also above 40")
    else:
        print("and above 40")