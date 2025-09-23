#A tuple is a collection which is ordered and unchangeable.

tup1=("apple","mango","banana","cheery","watermelon")
print("tupple 1=",tup1)
print("indexing =", tup1[4])
print("length of tupple=",len(tup1))
print("type of data=",type(tup1))

tup2=("apple",13,20.88,True)
print("tupple 2=",tup2)

tup=tuple(("apple",12,100.22))
print("tupple=",tup)
print("indexing",tup[2])
print("indexing",tup[-1])
print("indexing",tup[0:3])

if "apple" in tup:
    print("yess it is present")
    
#Convert the tuple into a list to be able to change it
y=list(tup)
y[2]="kiwi"
tup=tuple(y)
print("index 2=kiwi",tup)

y=list(tup)
y.append("watermelon")
tup=tuple(y)
print("appended tuple",tup)

#Add tuple to a tuple
q=("orange",102)
tup+=q
print("adding tuple to tuple",tup)

#Remove Items
y=list(tup)
y.remove("apple")
tup=tuple(y)
print("removing element form tuple",tup)

#Unpacking a tuple:
tup3=("apple","banana","kiwi")
(green,yellow,red)=tup3
print(green)
print(yellow)
print(red)
print("join  " ,tup1+tup2)
print("mltiply tuple ",tup1*3)
