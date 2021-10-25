class User:
    def __init__(self, name):
        self.name = name
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_user_balance(self):
        print(f"{self.name} Your balance is ${self.balance}")

    def transfer_money(self, amount, destination):
        self.balance -= amount
        destination.balance += amount
        destination.display_user_balance()
        return self

adrien = User("Adrien")
john = User("John")
wayne = User("Wayne")

adrien.deposit(500).deposit(1000).deposit(2000).withdraw(100).display_user_balance()

john.deposit(500).deposit(1000).withdraw(50).withdraw(150).display_user_balance()

wayne.deposit(1000).withdraw(100).withdraw(50).withdraw(50).display_user_balance()

john.transfer_money(100, wayne).display_user_balance()