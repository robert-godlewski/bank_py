# Go to user_bank_accounts.py to run this file
from bank_account import BankAccount


class User:
    def __init__(self, user_name):
        self.user_name = user_name
        self.checking_account = BankAccount(int_rate=0.01, balance=0)
        self.savings_account = BankAccount(int_rate=0.03, balance=0)

    def make_deposit(self, account, amount): return account.deposit(amount)

    def make_withdrawl(self, account, amount): return account.withdraw(amount)

    def display_user_balance(self): 
        details = f'''
        User: {self.user_name}, Checking {self.checking_account.display_account_info()}\n
        User: {self.user_name}, Savings {self.savings_account.display_account_info()}
        '''
        return details

    def transfer_money(self, other_user, account_from, account_to, amount):
        self.make_withdrawl(account_from, amount)
        other_user.make_deposit(account_to, amount)
        return self

    def transfer_between_accounts(self, account_from, account_to, amount):
        return self.transfer_money(self, account_from, account_to, amount)
