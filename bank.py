class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            self.balance += amount
            print(f"Deposited: £{amount}")
        else:
            print("Error: Deposit amount must be positive")

    def withdraw(self, amount):
        if int(amount) < 0 and amount <= self.balance:
            self.balance -= amount
            print(self.balance)
            return True
        else:
            return False

    def display_balance(self):
        print(f"Account Balance: £{self.balance}")

    def process_transaction(self, transaction_type, amount):
        if transaction_type.lower() == "deposit":
            self.deposit(amount)
        elif transaction_type.lower() == "withdraw":
            self.withdraw(amount)
        else:
            print("Error: Invalid transaction type")

account = BankAccount(12345678, 1000)

print("what would you like to do:")
print("1. withdraw")
print("2. deposit")
choice = input("Enter choice(1, 2):")

if choice == '1':
    account.process_transaction("withdraw", input("how much?"))
    account.withdraw()
elif choice == '2':
    account.process_transaction("deposit", input("how much?"))
else:
    print("Invalid choice")

account.withdraw()