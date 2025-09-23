# 🔹 Beginner Level
# Create a dictionary of 5 students with their marks. Print all keys and values separately.
# students = {"Alice": 85, "Bob": 72, "Charlie": 90, "David": 60, "Eva": 95}
# Print only the student names.
# Print only the marks.
# Print key-value pairs in a loop.
# Add a new student "Frank": 78 to the dictionary.
# Update "Bob"’s marks to 80.
# Delete "David" from the dictionary.
# 🔹 Intermediate Level
# Create a dictionary of countries and capitals.
# Ask the user to enter a country name.
# Print the corresponding capital if it exists, otherwise print "Not found".
# Merge two dictionaries:
# dict1 = {"a": 1, "b": 2}
# dict2 = {"c": 3, "d": 4}
# Expected result: {"a": 1, "b": 2, "c": 3, "d": 4}
# 🔹 Advanced Level
# Create a dictionary from two lists:
# keys = ["name", "age", "city"]
# values = ["Alice", 25, "New York"]
# Result: {"name": "Alice", "age": 25, "city": "New York"}
# You have a dictionary of students and their marks. Find the student(s) with the highest score.
# scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 92}
# Expected output: ["Bob", "David"]
# Write a program that takes a dictionary and inverts it (swap keys and values).
# Example:
# {"a": 1, "b": 2, "c": 3} → {1: "a", 2: "b", 3: "c"}


dict1={"Alice": 85, "Bob": 72, "Charlie": 90, "David": 60, "Eva": 95}
print(dict1)
print (dict1.keys())
print(dict1.values())
print(dict1.items())
dict1["Frank"]=78
print(dict1)
dict1["Bob"]=80
print(dict1)
dict1.pop("David")
print(dict1)

countries = {
    "India": "New Delhi",
    "USA": "Washington, D.C.",
    "France": "Paris",
    "Germany": "Berlin",
    "Japan": "Tokyo"
}

country=input("enter the country name")
if country in countries:
    print("The capital of", country, "is", countries[country])
else:
    print("Not found")
    
dict2 = {"a": 1, "b": 2}
dict3 = {"c": 3, "d": 4}
dict2.update(dict3)
print(dict2)

keys = ["name", "age", "city"]
values = ["Alice", 25, "New York"]
dict5=dict(zip(keys,values))
print(dict5)

scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 92}
max_score=max(scores.values())
top_students = []
for name, score in scores.items():
    if score == max_score:
        top_students.append(name)

print(top_students)