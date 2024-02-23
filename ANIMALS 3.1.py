import random
class Animal:
    def __init__(self, name, species, legs):
        self.name = name
        self.species = species
        self.legs = legs
    def voice(self):
        print(self.name, " подає голос")
    def move(self):
        print(self.name, " рухається")

class Dog(Animal):
    breed_list = {"Мопс", "Щпіц", "Шіба-Іну", "Такса"}
    breed = random.choice(list(breed_list))

    legs = 4
    wingspan = False
    species = "Dog"
    
    def __bark(self):
        print(self.name, " гавкає")

class Bird(Animal):
    legs = 2
    wingspan = True
    species = "Bird"

    def __fly(self):
        print(self.name," літає")



