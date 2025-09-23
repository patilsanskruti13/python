import math
print(math.cos(3.65))

#Arithmetic Operators

u=10
v=20
print("sum is",u+v)
print("sub is",u-v)
print("multiplication is",v*u)
print("divison is",v/u)
print("moduluds is",u%v)
print("Exponentiation is" ,v**u)
print("Floor division is",v//u)

#Assignment Operators

v += 3
print("sum",v)

v-=10
print("sub",v)

v*=40
print("multi",v)

v/=10
print("div",v)

v%=4
print("modulus",v)
t=35
t//=4 #division upto 2 decimal 
print(t)

t=66
t**=3 #20^3
print(t)

t &= 3
print(t)
h=22
h |= 3
print(h)

x = 5 
x ^= 3
print(x)

x = 5 
x >>= 3 
print(x)

print(type (v))

x = 5

x <<= 3

print(x)

#Comparison Operators
q=6
w=4
print(q==w)
print(q!=w)
print(q>w)
print(q<w)
print(q>=w)
print(q<=w)

#IDENTITY OPRRATOR

A=10
B=9
print("A=B",A is B)
print("A=!B",A is not B)