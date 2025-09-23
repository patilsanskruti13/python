def add(a,b):
    sum=a+b
    print(sum)
add(5,10)
def hello_world():
    print("hello world")
hello_world()

list1=["A","B","C","D","E","F","G"]
no=[1,2,3,4,5,6,7,8,9,10]

#print the length of list
def print_len(list):
    print(len(list))
print_len(list1)
print_len(no)

#to print the list
def print_list(list):
    for i in list:
        print(i,end=" ")
print_list(list1)
print_list(no)

#waf to find factorial of n
def cal_factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    print(fact)
cal_factorial(10) 

#waf to convert usd to inr
def converter(usd_val):
    inr_val=usd_val*83
    print(usd_val,"USD=",inr_val,"INR")
converter(100)      

#to identify the no. is odd or even
def odd_even(n):
    if n%2==0:
        print("even")
    else:
        print("odd")
odd_even(7) 


#RECURSION
def show(n):
    if(n==0):
        return
    print (n)
    show(n-1)
show(10)

def fact(n):
    if (n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)
print(fact(4))


#WRITE A RECURSIE FUN TO CALCULATE THE SUM OF FIRST N NATURAL NO.add()

def cal_sum(m):
    if (m==0):
        return 0
    
    return cal_sum(m-1) + m
sum = cal_sum(10)    
print(sum)


# write a recursive fun to print all the elements of list
list2=[11,22,33,44,55,66,77,88]

def print_list(list,idx):
    if (idx==len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)
    
print_list(list2,0)