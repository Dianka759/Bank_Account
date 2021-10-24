class BankAccount:
    accounts = []

    def __init__(self, name, int_rate, balance=0):
        self.name = name
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return self
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
            return self

    def display_account_info(self):
        print(f"Account: {self.name}, Balance: {self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        else:
            print("No interest acquired because balance is negative")
        return self

    @classmethod
    def print_all_accounts(cls):
        print("All instances of a Bank Account's info:")
        for account in cls.accounts:
            account.display_account_info()


# declaring two bank accounts
normal_people = BankAccount("Normal People",.03, 100)
me = BankAccount("Me",.15)

# making deposits, withdrawls, interest, and displaying ending balance
normal_people.deposit(1000).deposit(10).deposit(
    20).withdraw(15).yield_interest().display_account_info()
print()   # for visual purposes, to separate the two account balances
me.deposit(100).deposit(10).withdraw(100).withdraw(5).withdraw(
    5).withdraw(20).yield_interest().display_account_info()

print() # again, for visual purposes, to separate from the rest
BankAccount.print_all_accounts()