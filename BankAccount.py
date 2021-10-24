class BankAccount:
    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate
        self.balance = balance

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
        print("Balance:", self.balance)
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        else:
            print("No interest because balance is negative")
        return self

    # use a classmethod to print all instances of a Bank Account's info
    # @classmethod


normal_people = BankAccount(.03, 100)
me = BankAccount(.15)

normal_people.deposit(1000).deposit(10).deposit(
    20).withdraw(15).yield_interest().display_account_info()
print()   # for visual purposes, to separate the two account balances
me.deposit(100).deposit(10).withdraw(100).withdraw(5).withdraw(
    5).withdraw(20).yield_interest().display_account_info()
