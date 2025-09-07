class BankAccount:
    def __init__(self, accountnumber, accountholder, accountbalance=0):
        self.accountnumber = accountnumber
        self.accountholder = accountholder
        self.accountbalance = accountbalance

    def deposit(self, amount):
        if amount > 0:
            self.accountbalance += amount
            print("Deposited:", amount)

    def withdraw(self, amount):
        if amount > 0 and amount <= self.accountbalance:
            self.accountbalance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance..")

    def checkbalance(self):
        print("Current balance:", self.accountbalance)

    def get_accountnumber(self):
        print("Account Number:", self.accountnumber)

    def get_accountholder(self):
        print("Account Holder:", self.accountholder)


# Account details
accountnumber = "123123123"
accountholder = "Ram"
accountbalance = 3250

# Login process
while True:
    print("What is your account name?")
    name = input()
    if name != accountholder:
        continue
    print(f"Welcome {accountholder}, How may I assist you today.")
    break

# Create account object
ba = BankAccount(accountnumber, accountholder, accountbalance)

# Menu
print("Enter your query \n 1.Accountnumber \n 2.Deposit \n 3.Withdraw \n 4.Checkbalance")
intpot = int(input("Enter the query Number.....\n"))

if intpot == 1:
    ba.get_accountnumber()
elif intpot == 2:
    amount = int(input("Enter amount to deposit: "))
    ba.deposit(amount)
elif intpot == 3:
    amount = int(input("Enter amount to withdraw: "))
    ba.withdraw(amount)
elif intpot == 4:
    ba.checkbalance()
else:
    print("Invalid option")
