class Account:
    def __init__(self,number,pin):
        self.number=number
        self.__pin=pin
        self.__balance=0# The double underscore is to protect the numbers from being seen
    def check_balance(self,pin):
        if pin==self.__pin:
            return self.__balance
        else:
            return "wrong pin"
class Accounts:
    def __init__(self, account_owner, current_balance=0):
        self.account_owner = account_owner
        self.balance = current_balance
        # self.transactions = []
    def view_account_details(self):
        # """Display account owner's details and current balance."""
        print(f"Account Owner is {self.account_owner}")
        print(f"Current Balance is {self.balance}")
    def change_account_owner(self, new_owner):
        # """Update the account owner's information."""
        self.account_owner = new_owner
        print(f"Account owner changed to  {self.account_owner}")
    def account_statement(self,recent_transactions):
        # """Generate a statement of recent transactions."""
        # print("Recent Transactions:")
        # for transaction in self.transactions:
        #     print(f"{transaction['type']}: ${transaction['amount']:.2f}")
        self.recent_transactions=recent_transactions
        print(f"recent transactions is {self.recent_transactions}")
    def set_overdraft_limit(self, overdraft_limit):
        # """Set an overdraft limit for the account."""
        self.overdraft_limit = overdraft_limit
        print(f"Overdraft limit set to {self.overdraft_limit}")
    def calculate_interest(self, annual_interest_rate):
        # """Calculate and apply interest to the balance."""
        monthly_interest_rate = annual_interest_rate / 12 / 100
        interest_amount = self.balance * monthly_interest_rate
        self.balance += interest_amount
        print(f"Interest applied is ${interest_amount}")
    def freeze_account(self):
       # """Freeze the account for security reasons."""
       self.is_frozen = True
       print("Account frozen.")
    def unfreeze_account(self):
        # """Unfreeze the account."""
        self.is_frozen = False
        print("Account unfrozen.")
    def add_transaction(self, transaction_type, amount):
        # """Record a transaction."""
        self.transactions.append({"type": transaction_type, "amount": amount})
    def transfer_funds(self, target_account, amount):
        # """Transfer funds from this account to another account."""
        if self.balance >= amount:
            self.balance -= amount
            target_account.balance += amount
            self.add_transaction("Transfer Out", -amount)
            target_account.add_transaction("Transfer In", amount)
            print(f"${amount:.2f} transferred to {target_account.account_owner}.")
        else:
             print("Insufficient balance for transfer.")
    def close_account(self):
         # """Close the account and perform necessary cleanup."""
         self.balance = 0
         self.transactions = []
         print("Account closed.")


    if __name__ == "__main__":
      my_account = Accounts(account_owner="Jane", initial_balance=20000)
      my_account.view_account_details()
      my_account.change_account_owner("Mary Jane")
      my_account.calculate_interest(4.5)
      my_account.transfer_funds(target_account=my_other_account, amount=2500)
      my_account.add_transaction("Deposit", 3000)
      my_account.account_statement()
      my_account.close_account()