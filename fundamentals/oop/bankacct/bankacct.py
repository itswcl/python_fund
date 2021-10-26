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

andrew = BankAccount(0.015, 10000)
way = BankAccount(0.015, 5000)

andrew.desposit(100).desposit(100).desposit(100).withdraw(300).yield_interest().display_account_info()
way.desposit(200).desposit(400).withdraw(100).withdraw(100).withdraw(100).withdraw(100).yield_interest().display_account_info()
BankAccount.display_accounts()