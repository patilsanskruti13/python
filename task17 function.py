def create_acc():
    global acc_no,bal
    acc_no=int(input("Enter your acc no.:"))
    bal=int(input("Enter your account balance:"))
    print("account created successfully")
    
def check_bal():
    print("Your balance is :",bal)    
def withdraw():
    global bal
    withdraw=float(input("Enter the amount to withdraw="))
    if withdraw>bal:
        print("Insufficient Balance")  
    elif withdraw <= 0:
        print("Invalid withdrawal amount.")
    else:
        bal -= withdraw
        print("Withdrawal successful! Remaining balance: Rs.", bal)
        
def deposit():
    global bal
    deposit=float(input("Enter the amount to deposit="))
    if deposit>0:
        bal += deposit
        print("Deposit successful! New balance: Rs.", bal)
    else:
        print("Invalid deposit amount.")    
        
def main():
    print("===== ATM MENU =====")
    print("1. Create account")
    print("2. Check balance")
    print("3. Withdraw")
    print("4. Deposit")
    print("5. Exit")

    while True:
        ch = int(input("\nEnter your choice (1-5) = "))

        if ch == 1:
            create_acc()
        elif ch == 2:
            check_bal()
        elif ch == 3:
            withdraw()
        elif ch == 4:
            deposit()
        elif ch == 5:
            print(" Exiting... Goodbye!")
            break
        else:
            print(" Invalid choice! Please enter between 1–5.")  
            
main()