class User:
    def __init__(self, name):
        self.name = name
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        self.display_user_balance()

    def withdraw(self, amount):
        self.balance -= amount
        self.display_user_balance()

    def display_user_balance(self):
        print(f"{self.name} Your balance is ${self.balance}")

    def transfer_money(self, amount, destination):
        self.balance -= amount
        destination.balance += amount
        self.display_user_balance()
        destination.display_user_balance()


adrien = User("Adrien")
john = User("John")
wayne = User("Wayne")

adrien.deposit(500)
adrien.deposit(1000)
adrien.deposit(2000)
adrien.withdraw(100)

john.deposit(500)
john.deposit(1000)
john.withdraw(50)
john.withdraw(150)
john.display_user_balance()

wayne.deposit(1000)
wayne.withdraw(100)
wayne.withdraw(50)
wayne.withdraw(50)
wayne.display_user_balance()

john.transfer_money(100, wayne)
# john.display_user_balance()
# wayne.display_user_balance()