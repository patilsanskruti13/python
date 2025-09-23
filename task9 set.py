# 🔹 Set Tasks
# Create a set of 5 numbers and print it.
# Add a new element to a set and remove an existing element.
# Write a program to find the union and intersection of two sets.
# Create a set and check if a particular value exists in it.
# Convert a list with duplicate values into a set and display the result.
# Write a program to find the difference between two sets.
# Create two sets and check if one is a subset of the other.
# Remove all elements from a set using a method.
# Find the maximum and minimum values from a set of numbers.
# Use a set comprehension to create a set of squares of numbers from 1 to 10.

s1={1,2,3,4,5}
print("set=",s1)
s1.add(6)
print("adding to set=",s1)

s1.remove(3)
print("removing the element ",s1)

s1.discard(4)
print("removing the element using discard",s1)

s2={1,2,3,4,5,6,7,8}
s3={9,10,11,1,2,3,5,13,12}

s4=s2.union(s3)
print("union of set 2n 3 is ",s4)
s5=s2.intersection(s3)
print("intersection of set 2n3 is",s5)
s6=s2.difference(s3)
print("difference of set 2n 3 is",s6)

l=[1,2,3,4,2,4,5,2,4,3,6,7,8,6,7,9]
print("list with duplicate value is=",l)
set_1=set(l)
print("set w/o duplicate value is",set_1)

a={1,2,3,4,5,6,7,8,9}
b={12,6,7,11,12,13}
print("cheking the subset ", a.issubset(b))

b.clear()
print("set after clearing",b)

maximum=max(a)
minimum=min(a)

print("maximum no. is", maximum)
print("minimum no. is ",minimum)

# Create a set of squares using set comprehension
squares = {x**2 for x in range(1, 11)}

print("Set of squares from 1 to 10:", squares)
