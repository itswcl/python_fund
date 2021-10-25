class User():
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def display_user_balance(self):
        print(self.balance)

    def transfer_money(self, amount, destination):
        self.balance -= amount
        destination.balance += amount


adrien = User("Adrien", 500)
john = User("John", 1000)
wayne = User("Wayne", 100)

adrien.deposit(50)
adrien.deposit(100)
adrien.deposit(200)
adrien.withdraw(100)

john.deposit(50)
john.deposit(100)
john.withdraw(50)
john.withdraw(150)
john.display_user_balance()

wayne.deposit(100)
wayne.withdraw(100)
wayne.withdraw(50)
wayne.withdraw(50)
wayne.display_user_balance()

john.transfer_money(100, wayne)
john.display_user_balance()
wayne.display_user_balance()