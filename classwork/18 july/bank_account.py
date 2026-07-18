class BankAccount:

    def accept_details(self):
        self.account_number = input("Enter Account Number : ")
        self.customer_name = input("Enter Customer Name : ")
        self.balance = float(input("Enter Initial Balance : "))

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Amount Deposited Successfully.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("Amount Withdrawn Successfully.")
        else:
            print("Insufficient Balance")

    def display_balance(self):
        print("\n------ Account Details ------")
        print("Account Number :", self.account_number)
        print("Customer Name  :", self.customer_name)
        print("Current Balance :", self.balance)


# Create an object of BankAccount class
account1 = BankAccount()

# Accept account details
account1.accept_details()

# Accept deposit amount
deposit_amount = float(input("Enter Deposit Amount : "))
account1.deposit(deposit_amount)

# Accept withdrawal amount
withdraw_amount = float(input("Enter Withdrawal Amount : "))
account1.withdraw(withdraw_amount)

# Display final account details and balance
account1.display_balance()