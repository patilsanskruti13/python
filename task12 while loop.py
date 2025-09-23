# # Program to print numbers until user enters 0

num = int(input("Enter a number (0 to stop): "))

while num != 0:
    print("You entered:", num)
    num = int(input("Enter a number (0 to stop): "))

print("Program stopped because you entered 0.")


# # Popping out elements from a list using while loop 
# # fruitsList = ["Mango","Apple","Orange","Guava"]
fruitsList = ["Mango","Apple","Orange","Guava"]
while fruitsList:  
    fruit = fruitsList.pop()  
    print("Popped:", fruit)

print("All fruits have been removed.")

# # Finding the average of 5 numbers using while loop
count=0
total=0
while count<=5:
    num=float(input("enter the number"))
    total+=num
    count+=1
    
avg=total/5
print("the average is ", avg)

# Finding the sum of even numbers using while loop first 10 numbers

# total=0
# count=1
# num=2
# while count<=10:
#     total+=num
#     num+=2
#     count+=1
# print("sum of even no. are ", total)

# name = 'Jesaa29Roy'
# i = 0

# while i < len(name):
#     char = name[i]
#     if char.isdigit():   
#         break
#     print(char)
#     i += 1

# Write a Python program to display only those numbers from a list that
# satisfy the following conditions
# The number must be divisible by five
# If the number is greater than 150, then skip it and move to the following 
# number
# If the number is greater than 500, then stop the loop
# numbers = [12, 75, 150, 180, 145, 525, 50]   use break,contiunue,pass

numbers = [12, 75, 150, 180, 145, 525, 50]

for num in numbers:
    if num > 500:
        break        
    elif num > 150:
        continue     
    elif num % 5 == 0:
        pass         
        print(num)