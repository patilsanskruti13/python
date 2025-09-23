"""
class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    # Debit method
    def debit(self, amount):
        if amount > self.balance:
            print("Insufficient balance! Transaction failed.")
        else:
            self.balance -= amount
            print("Rs", amount, "was debited")
            print("Total balance =", self.get_balance())

    # Credit method
    def credit(self, amount):
        self.balance += amount
        print("Rs", amount, "was credited")
        print("Total balance =", self.get_balance())

    # Get balance method
    def get_balance(self):
        return self.balance


# Main Program
acc1 = Account(10000, 1234)
print("Account created successfully!")
print("Account Number:", acc1.account_no)
print("Initial Balance:", acc1.balance)

while True:
    print("\n--- MENU ---")
    print("1. Debit Money")
    print("2. Credit Money")
    print("3. Check Balance")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amt = float(input("Enter amount to debit: "))
        acc1.debit(amt)
    elif choice == 2:
        amt = float(input("Enter amount to credit: "))
        acc1.credit(amt)
    elif choice == 3:
        print("Current Balance =", acc1.get_balance())
    elif choice == 4:
        print("Thank you! Exiting...")
        break
    else:
        print("Invalid choice! Please try again.")"""
class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    # Class method to create account
    @classmethod
    def create_account(cls):
        acc_num = int(input("Enter new Account Number: "))
        init_bal = float(input("Enter Initial Balance: "))
        return cls(init_bal, acc_num)

    # Debit method
    def debit(self, amount):
        if amount > self.balance:
            print("Insufficient balance! Transaction failed.")
        else:
            self.balance -= amount
            print("Rs", amount, "was debited")
            print("Total balance =", self.get_balance())

    # Credit method
    def credit(self, amount):
        self.balance += amount
        print("Rs", amount, "was credited")
        print("Total balance =", self.get_balance())

    # Get balance method
    def get_balance(self):
        return self.balance


# Main Program
print("=== Create a New Account ===")
acc1 = Account.create_account()
print("\n✅ Account created successfully!")
print("Account Number:", acc1.account_no)
print("Initial Balance:", acc1.balance)

while True:
    print("\n--- MENU ---")
    print("1. Debit Money")
    print("2. Credit Money")
    print("3. Check Balance")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amt = float(input("Enter amount to debit: "))
        acc1.debit(amt)
    elif choice == 2:
        amt = float(input("Enter amount to credit: "))
        acc1.credit(amt)
    elif choice == 3:
        print("Current Balance =", acc1.get_balance())
    elif choice == 4:
        print("Thank you! Exiting...")
        break
    else:
        print("Invalid choice! Please try again.")
