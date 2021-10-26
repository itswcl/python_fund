class User:
    def __init__(self, name):
        self.name = name
        self.account = BankAccount(int_rate = 0.02, balance = 0)

    def deposit(self, amount):
        self.account.deposit(amount)
        return self

    def withdraw(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        print(f"{self.name} Your balance is ${self.account.balance}")
        return self

    # def transfer_money(self, amount, destination):
    #     self.account.balance -= amount
    #     destination.account.balance += amount
    #     return self


class BankAccount:
    all_accounts = []
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
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

andy = User("andy").deposit(100).display_user_balance()
paul = User("paul").deposit(500).display_user_balance()