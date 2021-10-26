class BankAccount:
    all_accounts = []
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def desposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance < amount:
            self.balance -= 5
            print("Insufficient funds: Charging a $5 fee")
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self

    @classmethod
    def display_accounts(cls):
        for account in cls.all_accounts:
            account.display_account_info() # access each account status

class User:
    def __init__(self, name):
        self.name = name
        self.account = {
            "saving": BankAccount(0.05, 5000),
            "checking": BankAccount(0.01, 1000)
        }

    def transfer_money(self, amount, destination):
        self.balance -= amount
        destination.balance += amount
        destination.display_user_balance()
        return self

andrew = User("andrew")
# print(andrew.name)
# print(andrew.account["saving"].balance)
# print(andrew.account["checking"].balance)
# andrew.account["checking"].desposit(100)
# andrew.account["checking"].withdraw(50)
# andrew.account["saving"].desposit(5000)
# andrew.account["checking"].display_account_info()
# andrew.account["saving"].display_account_info()
andrew.account["checking"].display_account_info()
andrew.account["saving"].display_account_info()