# 🔹 Tuple Tasks
# Create a tuple of 5 different fruits and print the first and last elements.
# Write a program to find the length of a tuple without using len().
# Concatenate two tuples and display the result.
# Create a tuple with mixed data types (string, int, float, list) and print each element with its type.
# Write a program to check if a given element exists in a tuple.
# Convert a tuple into a list, modify one element, and convert it back into a tuple.
# Create a nested tuple and access an element from the inner tuple.
# Find the index of a given element in a tuple.
# Count how many times a specific value appears in a tuple.
# Unpack a tuple into individual variables and print them.
tup1=("apple","banana","cherry","mango","grapes")
print("tuple 1=",tup1)
print("length of tuple 1=",len(tup1))
tup2=(1,2,3,4,5)
tup3=tup1+tup2
print("concatinated tuple =", tup3)
tup4=(1,23,22.5,"a",[1,2,3])
for x in tup4:
    print("data type of element is ",type(x))
    
if "banana" in tup1:
    print("yes it is present in tuple")
    
l1=list(tup1)
l1[2]="watermelon"
tup1=tuple(l1)
print("convertig tuple to list n again to tuple",tup1)
print(type(tup1))

nested_tup=(1,2,3,4,(5,6,7,8))
print("accessing the element of nested tuple",nested_tup[4][3])
inner_tup=nested_tup[4]
print("inner tuple is =",inner_tup)

print("finding the index of watrmelon=",tup1.index("watermelon"))
print("finding the index of 5,6,7,8=",nested_tup.index((5,6,7,8)))

tup=(1,2,3,4,5,1,7,8,9,1,22,33,22,33,33,33,33,33)
print("no. of occurence of 33", tup.count(33))

tupa=(1,2,3,4)
(x,y,*z)=tupa
print(x)
print(y)
print(z)