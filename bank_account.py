class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self): return "Balance: $" + str(self.balance)

    def yield_interest(self): 
        if self.balance > -1:
            interest = self.balance * self.int_rate
            return self.deposit(interest)
        else:
            return self


# Testing
robert = BankAccount(0.03, 1000)
joe = BankAccount(0.03, 2000)

print(robert.deposit(100000).deposit(50000).deposit(50000).withdraw(5000).yield_interest().display_account_info())
print(joe.deposit(10000).deposit(100000).withdraw(1000).withdraw(1000).withdraw(1000).withdraw(1000).yield_interest().display_account_info())
