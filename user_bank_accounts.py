# main program that runs both user and bank_account classes
from user import User


robert = User("Robert")
rob_check = robert.checking_account
rob_save = robert.savings_account

robert.make_deposit(rob_check, 100000)
robert.transfer_between_accounts(rob_check, rob_save, 50000)
robert.make_withdrawl(rob_check, 25000)
print(robert.display_user_balance())
