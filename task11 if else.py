#1. Write a program that takes a student's score (0-100) and prints their grade:
# - A: 90-100
# - B: 80-89
# - C: 70-79
# - D: 60-69
# - F: Below 60
# marks=int(input("enter the marks"))

# if marks>=90 and marks<=100:
#     print("grade=A")
# elif marks>=80 and marks<=89:
#     print("grade=B")
# elif marks>=70 and marks<=79:
#     print("grade=C")
# elif marks>=60 and marks<=69:
#     print("grade=D")
# else:
#     print("grade=F")
# 2.Write a program that determines if a year is a leap year.

# yr=int(input("Enter the year"))

# if yr%400==0:
#     print("leap year")
# elif yr%100==0:
#     print("not a leap year")
# elif yr%4==0:
#     print("leap year")
# else :
#     print("not a leap year")        

# 3.write program to find max number from 3 numbers
# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
# c = int(input("Enter the third number: "))

# if a>=b and a>=c:
#     print("a is greater")
# elif b>=a and b>=c:
#     print("b is greater")    
# else:
#     print("c is greater")
    
# 4.write program to check weather character is vowel or not

# ch = input("Enter a character: ")
# ch = ch.lower()
# if ch in ['a', 'e', 'i', 'o', 'u']:
#     print("The character is a vowel.")
# else:
#     print("The character is not a vowel.")

# 5.Python program to check if the number is divisible by 5 or not
# no=int(input("enter the no. to check if it is divisible by 5 or not"))
# if no%5==0:
#     print("divisible by 5")
# else:
#     print("not divisible by 5")

#  6 check weather string is palindrom or not
# text=input("enter your text = ")
# text=text.lower()

# if text==text[::-1]:
#     print("string is palindrome")
# else:
#     print("string is not palindrome")
# 7.Write a program that will ask the user the following question:
# Is Sydney the capital of Australia?
# If the user answers y, print: Wrong! Canberra is the capital!
# If the user answers n, print: Correct!
# If the user answers anything else, print: I do not understand your answer!

print("Is Sydney the capital of Australia?")
ans=input("Enter your ans (y/n)=")
ans=ans.lower()
if ans=="y":
    print("Wrong! Canberra is the capital!")
elif ans=="n":
    print("Correct!")  
else:
    print("I do not understand your answer!")  


