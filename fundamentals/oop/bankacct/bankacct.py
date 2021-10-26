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
        self.balance -= amount
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")

    def yield_interest(self):
        self.balance += self.balance * self.int_rate
        return self

    @classmethod
    def display_accounts(cls):
        for value in cls.all_accounts:
            print(value)

andrew = BankAccount(0.015, 10000)
way = BankAccount(0.015, 5000)

andrew.desposit(100).desposit(100).desposit(100).withdraw(300).yield_interest().display_account_info()
way.desposit(200).desposit(400).withdraw(100).withdraw(100).withdraw(100).withdraw(100).yield_interest().display_account_info()
BankAccount.display_accounts()