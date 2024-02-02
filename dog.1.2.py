import random

class Dog:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.satiety = 50
        self.energy = 50
        self.alive = True

    def to_walk(self):
        print("Треба прогулятись!")
        self.gladness += 10
        self.satiety -= 3
        self.energy -= 8

    def to_sleep(self):
        print("Час поспати...")
        self.energy += 10
        self.satiety -= 5

    def to_eat(self):
        print(name," голодний, треба поїсти!")
        self.gladness += 3
        self.satiety += 6
        self.energy += 2


    def is_alive(self):
        if self.gladness < 0:
            print("У ",name," почалась депресія...")
            self.alive = False
        elif self.satiety < 0:
            print(name," помер з голоду")
            self.alive = False
        elif self.satiety > 100:
            print(name," помер через ожиріння")
            self.alive = False



    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Satiety = {self.satiety}")
        print(f"Energy = {self.energy}")

    def life(self, day):
        d = "Day ",str(day)," of ",self.name," life"
        print(f"{day:=^50}")
        life_rand = random.randint(1, 3)
        if life_rand == 1:
            self.to_eat()
        elif life_rand == 2:
            self.to_sleep()
        elif life_rand == 3:
            self.to_walk()
        self.end_of_day()
        self.is_alive()



name = input("Придумайте ім'я для цуценя:")
dog = Dog(name=name)
for i in range(1, 365):
    if dog.alive == False:
        break
    dog.life(i)

