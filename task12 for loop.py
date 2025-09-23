print("first")
for i in range(1,6):
    for j in range(1,i+1):
        print("*", end="")
    print()
print("second")    
for i in range(1,6):
    for j in range(1,i+1):
        print(j, end="")
    print()
print("third") 
for i in range(6,1,-1):
    for j in range(1,i):
        print(j, end="")
    print()
print("fourth") 
for i in range (1,6):
    for j in range(1,i+1):
        print(i,end="")
    print()