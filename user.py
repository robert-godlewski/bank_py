class User:
    def __init__(self, user_name, balance): 
        self.user_name = user_name
        self.balance = balance

    def make_deposit(self, amount): 
        self.balance += amount
        return self.balance

    def make_withdrawl(self, amount):
        self.balance -= amount
        return self.balance

    def display_user_balance(self):
        return "User: " + str(self.user_name) + ", Balance: " + str(self.balance)

    def tansfer_money(self, to_user, amount):
        self.balance -= amount
        to_user.balance += amount


# Testing
rob_bal = User('rob', 500)
nate_bal = User('nate', 50)
tristan_bal = User('tristan', 5)

rob_bal.make_deposit(10000)
rob_bal.make_deposit(5000)
rob_bal.make_withdrawl(1000)
rob_bal.make_deposit(500)
print(rob_bal.display_user_balance())

nate_bal.make_deposit(500000)
nate_bal.make_withdrawl(2000)
nate_bal.make_deposit(5000)
nate_bal.make_withdrawl(700)
print(nate_bal.display_user_balance())

tristan_bal.make_deposit(5000)
tristan_bal.make_withdrawl(500)
tristan_bal.make_withdrawl(5)
tristan_bal.make_withdrawl(100)
print(tristan_bal.display_user_balance())

rob_bal.tansfer_money(tristan_bal, 100)
print(rob_bal.display_user_balance())
print(tristan_bal.display_user_balance())
