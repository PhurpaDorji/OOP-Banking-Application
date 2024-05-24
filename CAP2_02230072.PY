import random
import os

# Define the bankaccount class
class BankAccount:
    # Initialize the Bankaccounts with Account number, Password, Balance and Account type 
    def __init__(self, account_number, password, balance=0, account_type="Personal"):
        self.account_number = account_number
        self.password = password
        self.balance = balance
        self.account_type = account_type

#stradegy to deposit amounts
    def deposit(self, amount):
        self.balance += amount
        return f"Deposit successful. New balance: {self.balance}"

# stradegy to withdraw amounts
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return f"Withdrawal successful. New balance: {self.balance}"
        else:
            return "Insufficient funds"

# stradegy to transfer the cash
    def transfer(self, amount, recipient_account):
        if self.balance >= amount:
            self.balance -= amount
            recipient_account.balance += amount
            return f"Transfer successful. New balance: {self.balance}"
        else:
            return "Insufficient funds"

    def delete_account(self):
        # To delete the account if desire
        with open("accounts.txt", "r") as f:
            lines = f.readlines()
        with open("accounts.txt", "w") as f:
            for line in lines:
                if str(self.account_number) not in line:
                    f.write(line)
        return "Account deleted successfully"


#define the personal accounts subclass inheriting from bankaccounts class
class PersonalAccount(BankAccount):
    def __init__(self, account_number, password, balance=0):
        super().__init__(account_number, password, balance, account_type="Personal")


# to difine business account subclass inheriting from bankaccount class
class BusinessAccount(BankAccount):
    def __init__(self, account_number, password, balance=0):
        super().__init__(account_number, password, balance, account_type="Business")


#function to create a new accounts if user's desire
def create_account(account_type="Personal"):
    #generate random account
    account_number = random.randint(10000, 99999)
    password = "default_password"  # generate a random password if needed by user
    # Create the PersonalAccount or BusinessAccount based on the specified type
    account = PersonalAccount(account_number, password) if account_type == "Personal" else BusinessAccount(account_number, password)
    with open("accounts.txt", "a") as f:
        f.write(f"{account.account_number} {account.password} {account.account_type} {account.balance}\n")
    return account

#login to an existing account

def login(account_number, password):
    with open("accounts.txt", "r") as f:
        for line in f:
            acc_num, acc_password, acc_type, acc_balance = line.strip().split()
            if acc_num == str(account_number) and acc_password == password:
                return BankAccount(int(acc_num), acc_password, int(acc_balance), acc_type)
    return None


#Function to to control the programe
def main():
    while True:
        #Display option
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

#act action based on user choice
        if choice == "1":
            account_type = input("Enter account type (Personal/Business): ")
            account = create_account(account_type)
            print(f"Account created successfully. Account number: {account.account_number}, Password: {account.password}")

        elif choice == "2":
            account_number = int(input("Enter account number: "))
            password = input("Enter password: ")
            account = login(account_number, password)
            if account:
                print("Login successful")
                while True:

                    # submenu options
                    print("\n1. Deposit")
                    print("2. Withdraw")
                    print("3. Transfer")
                    print("4. Delete Account")
                    print("5. Logout")
                    sub_choice = input("Enter your choice: ")
                    if sub_choice == "1":
                        amount = int(input("Enter amount to deposit: "))
                        print(account.deposit(amount))
                    elif sub_choice == "2":
                        amount = int(input("Enter amount to withdraw: "))
                        print(account.withdraw(amount))
                    elif sub_choice == "3":
                        recipient_account_number = int(input("Enter recipient's account number: "))
                        amount = int(input("Enter amount to transfer: "))
                        recipient_account = login(recipient_account_number, "")  # No need to check password for recipient
                        if recipient_account:
                            print(account.transfer(amount, recipient_account))
                        else:
                            print("Recipient account not found")
                    elif sub_choice == "4":
                        print(account.delete_account())
                        break
                    elif sub_choice == "5":
                        break
                    else:
                        print("Invalid choice")

            else:
                print("Invalid account number or password")

        elif choice == "3":
            break

        else:
            print("Invalid choice")

  #enter point of programe          

if __name__ == "__main__":
    main()
