#KIST IS MUTABLE THAT MEANS WE CAN CHANGE THE VALUES IN LIST OR ADD

import math
#LIST 
list1 = ["apple", "banana", "cherry", "apple", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list4 = ["abc", 34, True, 40, "male"]
print("list1",list1)

print(len(list1))

print("list2",list2)

print("list3",list3)

print("list4",list4)

print(list4[2])

print(list4[1])

print(list1[1:4])

list1[2]="mango"
print("changin",list1)

list1[2:4]="papaya","watermelon"
print(list1)
print("list2=",list2)
list2.insert(3,10)
print("insert",list2)

list5 = ["apple", "banana", "cherry"]
list5.append("orange")
print(list5)

list5.remove("apple")
print(list5)

list5.pop(1)
print("pop",list5)

list5.pop()
print(list5)

list6=[133,14,155,131,160,18]
del list6[2]
print(list6)
#sort
list6.sort()
print ("sorted list",list6)

print ("descending order")
list6.sort(reverse=True)
print (list6)

print ("ascending order")
list6.sort(reverse=False)
print (list6)

print("for loop")
for tt in list6:
    print("for loop",tt)
for i in range (len(list6)):
    print("for loop range",list6[i])
    
j=0
while j<(len(list6)):
    print(list6[j])    
    j=j+1
list7=["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in list7:
  if "a" in x:
    newlist.append(x)

print(newlist)
newlist = [x for x in list7 if "a" in x]

print(newlist)
newlist = [x for x in range(10)]

print(newlist)

newlist = [x for x in range(10) if x < 5]

print(newlist)

list7.reverse()
print(list7)
# copy 
list8=list7.copy()
print(list8)
list9=list(list8)
print(list9)
list10=list9[2:5]
print (list10)

#JOINING list
listt=list9+list10
print(listt)
listt.extend(list10)
print(listt)

print(list6)
print(list2)
for x in list6:
    list2.append(x)
print(list2)

print("count",listt.count("apple"))
print("index",listt.index("cherry"))