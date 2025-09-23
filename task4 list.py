l=[1,2,3,4,9,8,7,6,5,10,11,14]
print(l)
sum=0
multi=1
for x in l:
    sum+=x
    multi*=x
print("sum of values is=",sum)
print("Multiplication of values is= ",multi)

l.sort()
print(l)

print("Largest item in the list is =",l[-1])
print("smallest item in the list is =",l[0])

print(len(l))

if len(l)==0:
    print("list is empty")
else:
    print("list is not empty")
cloned=l.copy()
print("cloned list is=",cloned)
