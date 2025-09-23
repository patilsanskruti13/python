#UNORDERED , NO DUPLICATE VALUES
set1={"apple","cherry","banana","apple","grapes","papaya",1,2,3,4,5,6}
print(set1)
set2=set(("apple", "banana", "cherry","watermelon"))
print(set2)

for x in set2:
    print(x)
    
print("banana" in set2)
print("apple" not in set2)

#ADDING TO SET
set2.add("orange")
print(set2)

set2.update(set1)
print(set2)

#Add elements of a list to at set:
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

#REMOVE
set2.remove("apple")
print(set2)
 
set2.discard("banana")
print(set2)

set2.pop()
print(set2)

#LOOP SET for x in set2:
for x in set2:
    print("values of set 2 are",x)

#JOIN SETS
#UNION
set3=set1.union(set2)
print(set3)
set3=set1|set2       #use the | operator instead of the union()
print("union using |",set3)
#UPDATE

set11 = {"a", "b" , "c",1,2}
set22 = {1, 2, 3,3,2,"a"}

set11.update(set22)
print("set11 after updating",set11)

#INTERSECTION
print("intersection",set11.intersection(set22))
print("intersection using &",set11 & set22)

#difference

print("diff is=",set11.difference(set22))    #Keep all items from set1 that are not in set2
