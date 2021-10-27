from pets import Pet

class Ninja:
# implement __init__( first_name , last_name , treats , pet_food , pet )
    def __init__(self, first_name, last_name, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = Pet(name="", type="", tricks="")
# implement the following methods:
# walk() - walks the ninja's pet invoking the pet play() method
    def walk(self):
        self.pet.play()
# feed() - feeds the ninja's pet invoking the pet eat() method
    def feed(self):
        self.pet.eat()
# bathe() - cleans the ninja's pet invoking the pet noise() method
    def bathe(self):
        self.pet.noise()

user1 = Ninja("Wei", "Lee", "Biscuit", "Meat")
user1.pet = Pet("Louis", "dog", "fetch", 10, 5)

user1.feed()
user1.walk()
user1.bathe()

print(user1.pet.energy)
print(user1.pet.health)