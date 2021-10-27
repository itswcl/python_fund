class Pet:
# implement __init__( name , type , tricks ):
    def __init__(self, name, type, tricks, health=0, energy=0):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy
# implement the following methods:
# sleep() - increases the pets energy by 25
    def sleep(self):
        self.energy += 25
# eat() - increases the pet's energy by 5 & health by 10
    def eat(self):
        self.energy += 5
        self.health += 10
# play() - increases the pet's health by 5
    def play(self):
        self.health += 5
# noise() - prints out the pet's sound
    def noise(self):
        print("ROAR ROAR ROAR")

class Dog(Pet):
    def __init__(self, name, type, tricks, health=0, energy=0):
        super().__init__(name, type, tricks, health=health, energy=energy)
        self.type = "Dog"
    def noise(self):
        print("HOWL HOWL HOWL")