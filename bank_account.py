# Go to user_bank_accounts.py to run this file
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
        else: return self
