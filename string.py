import math
#SLICING
b = " Hello, World! "
print(b[2:6])
print(b[:5])
print(b[2:])
print(b.upper())
print(b.lower())
print(b.strip())    #removes white space from start and end
print(b.replace("H","J")) #replaces a string with another string:
print(b.split(","))

aa = "Hello"
bb = "World"
cc = aa + " " + bb
print(cc)

age=22
txt=f"my name is sans & i'm {age}"
print(txt)

print("hello World".capitalize())
#print("hello world".title())
print("hello world".upper())
print("HELLO".casefold()) # hello
print("hi".center(10, '-'))
print("banana".count("a"))
print("python".endswith("on"))
print("H\tE\tL\tL\tO".expandtabs(4))
print("hello world".find("world"))
print("My name is {}".format("Alice"))
print("hello".index("e"))
print("hi".ljust(10, '-')) # hi--------
print("hello".rjust(10,'_'))
print("     hello     ".lstrip()) # 'hello'
print("     hello     ".rstrip())

name,address=input("enter name and address:").split(',')
print("my name is",name)
print("address is",address)
