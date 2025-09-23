dictt={"apple":"red" , 
       "orange":"org",
       "papaya":"yellow",
       "watermelon":"green"}
print(dictt)
print(dictt["apple"])
print(len(dictt))
print(type(dictt))

thisdict=dict(name = "sanskruti" , 
              age = 22 , 
              adress = "nashik ")
print(thisdict)
print(thisdict.get("age"))
print(thisdict.keys())


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change
# adding to dict
car["color"] = "white"

print(x) #after the change
print(car)
print(car.values())
print(car.items())

#CHANGING VALUES
car["color"]="red"
print(car)

car.update({"color":"pink"})
print(car)

car.pop("color")
print(car)
car.popitem()
print(car)
del car["model"]
print(car)

#copy dict

x=car.copy()
print(x)

y=dict(car)
print(y)










































