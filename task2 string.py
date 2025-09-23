s="Sumago @ 123"
countt=len(s)
print("length of string is",countt)
sp=0
summ=0
di=0
for x in s:
    if x.isdigit():
        di+=1
        summ+=int(x)
    elif not x.isalnum() and x!=" ":
        sp+=1
print("no. of digit=",di)
print("no. of special charachter is=",sp)
print("sum of digit are =",summ)



print("lower=",s.lower())
print("upper=",s.upper())
print("capitalize=",s.capitalize())
