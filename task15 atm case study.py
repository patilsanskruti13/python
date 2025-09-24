print("ATM")
print("1. Create account")
print("2.Check balance")
print("3.Withdraw")
print("4.Deposit")
print("5.Exit")


while True:
    ch=int(input("Enter your choice(1-5)="))
    
    if ch==1:
        acc_no=int(input("enter your account no.="))
        bal=float(input("Enter your account balance="))
        print("Account created successfully")
        
    elif ch==2:
        print(" Your account balance is = Rs.", bal)
    
    elif ch==3:
        withdraw=float(input("Enter the amount to withdraw="))
        if withdraw>bal:
            print("Insufficient Balance")  
        elif withdraw <= 0:
            print("Invalid withdrawal amount.")
        else:
            bal -= withdraw
            print("Withdrawal successful! Remaining balance: Rs.", bal)
            
    elif ch==4:
        deposit=float(input("Enter the amount to deposit="))
        if deposit>0:
            bal += deposit
            print("Deposit successful! New balance: Rs.", bal)
        else:
            print("Invalid deposit amount.")
  
    elif ch==5:    
        print("Exiting... Goodbye!")
        break

    else:
        print("Invalid choice! Please enter between 1–5.")