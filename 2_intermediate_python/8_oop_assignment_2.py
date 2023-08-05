# Build a Python class to represent a simple banking system. Create a class for a
# BankAccount, and another for Customer. The BankAccount class should have a
# constructor to initialize the account details (account number, balance, account type).
# The Customer class should have a constructor to set the customer's details (name,
# age, address) and create a BankAccount object for each customer. Implement a
# destructor for both classes to display a message when objects are destroyed.

class BankAccount:
    def __init__(self, account_number, balance, account_type):
        self.account_number = account_number
        self.balance = balance
        self.account_type = account_type

    def __del__(self):
        print(f"Bank account {self.account_number} of type {self.account_type} is being deleted.")


class Customer:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
        self.bank_account = None

    def create_bank_account(self, account_number, balance, account_type):
        self.bank_account = BankAccount(account_number, balance, account_type)

    def __del__(self):
        print(f"Customer {self.name} with bank account number {self.bank_account.account_number} is being deleted.")



# Create a customer and their bank account
customer1 = Customer("Raj Kumar Biswokarma", 26, "Rupandehi")
customer1.create_bank_account("123456789", 5000.00, "Savings")

# Display customer details and bank account info
print("Customer Details:")
print(f"Name: {customer1.name}")
print(f"Age: {customer1.age}")
print(f"Address: {customer1.address}")
print(f"Account Number: {customer1.bank_account.account_number}")
print(f"Balance: {customer1.bank_account.balance}")
print(f"Account Type: {customer1.bank_account.account_type}")

# Deleting the customer object will also trigger the deletion of the associated bank account object.
del customer1
