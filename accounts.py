# class Account:
#     def __init__(self,number,pin):
#         self.number=number
#         self.__pin=pin
#         self.__balance=0# The double underscore is to protect the numbers from being seen
#     def check_balance(self,pin):
#         if pin==self.__pin:
#             return self.__balance
#         else:
#             return "wrong pin"
class Account:
    def __init__(self, account_owner, current_balance=0):
        self.account_owner = account_owner
        self.balance = current_balance
        self.transactions = []
        self.frozen = False
        self.overdraft_limit=0

    def deposit(self,amount):
        if self.frozen:
            print("Account is frozen. Cannot proceed to deposit")
        self.balance+=amount
        self.transactions.append(f"Deposited: {amount}")
    def withdraw(self,withdraw_amount):
        if self.frozen:
            print("Account is frozen,You cannot withdraw")
        elif  withdraw_amount>(self.balance+self.overdraft_limit):
            print("Insufficient funds")   
        else:
            self.balance-=withdraw_amount
            self.transactions.append(f"Withdrawal:{-withdraw_amount}")
    def view_account_details(self):
        print(f"Account Owner is {self.account_owner} and the balance is {self.balance}")
        
    def change_account_owner(self, new_owner):
        if self.frozen:
            print("Cannot change the account the account is frozen")
        self.account_owner = new_owner
        print(f"Account owner changed to  {self.account_owner}")
    def account_statement(self):
        # """Generate a statement of recent transactions."""
        # print("Recent Transactions:")
         print(self.transactions)
    def set_overdraft_limit(self, limit):
        # """Set an overdraft limit for the account."""
        self.overdraft_limit = limit
        print(f"Overdraft limit set to {self.overdraft_limit}")
    def calculate_interest(self, rate):
        # """Calculate and apply interest to the balance."""
        interest_amount = self.balance * rate/100
        self.deposit(interest_amount)
    def freeze_account(self):
       # """Freeze the account for security reasons."""
       self.frozen = True
       print("Account frozen.")
    def unfreeze_account(self):
        # """Unfreeze the account."""
        self.frozen = False
        print("Account unfrozen.")
    def add_transaction(self, transaction_type, amount):
        # """Record a transaction."""
        self.transactions.append({"type": transaction_type, "amount": amount})
    def transfer_funds(self, target_account, amount):
        # """Transfer funds from this account to another account."""
        if self.frozen:
            print("The account is frozen")
        elif amount>self.balance:
            print("Insufficient balance")
        else:
            target_account + amount
    def close_account(self):
         # """Close the account and perform necessary cleanup."""
         self.balance = 0
         self.transactions = []
         print("Account closed.")


my_account = Account(account_owner="Jane",current_balance=20000)
my_account.view_account_details()
my_account.change_account_owner("Mary Jane")
my_account.calculate_interest(4.5)
my_account.transfer_funds(target_account="01AS380990909", amount=2500)
my_account.add_transaction("Deposit", 3000)
my_account.account_statement()
my_account.close_account()