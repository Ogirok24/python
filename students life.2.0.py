import random


class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 30
        self.progress = 0
        self.money = 30
        self.satiety = 30
        self.energy = 20
        self.alive = True

    def to_study(self):
        print("Time to study!")
        self.progress += 0.15
        self.gladness -= 2
        self.money -= 1
        self.satiety -= 3
        self.energy -= 2

    def to_sleep(self):
        print("I will sleep...")
        self.energy += 10
        self.satiety -= 3

    def to_chill(self):
        print("Rest time")
        self.gladness += 6
        self.progress -= 0.1
        self.money -= 5
        self.energy -= 4

    def to_eat(self):
        print("I'm hungry... I'm going to cook Mivina!")
        self.gladness += 1
        self.money -= 5
        self.satiety += 10
        self.energy += 1

    def to_work(self):
        print("I have no money... I will go to work")
        self.gladness -= 3
        self.money += 20
        self.satiety -= 3
        self.energy -= 3

    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out...")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression...")
            self.alive = False
        elif self.progress > 5:
            print("Passed externally")
            self.alive = False
        elif self.satiety < 0:
            print("Starvation...")
            self.alive = False
        elif self.satiety > 100:
            print("Adiposity...")
            self.alive = False

    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress), 1}")
        print(f"Money = {self.money}")
        print(f"Satiety = {self.satiety}")
        print(f"Energy = {self.energy}")

    def live(self, day):
        d = "Day " + str(day) + " of " + self.name + " life"
        print(f"{day:=^50}")
        rand = random.randint(1, 5)
        if self.money <= 5 and rand >= 4:
            self.to_work()
        elif self.satiety <= 10 and rand >= 3:
            self.to_eat()
        elif self.energy <= 10 and rand <= 3:
            self.to_sleep()
        elif self.gladness <= 10 and rand <= 3:
            self.to_chill()
        else:
            self.to_study()

        self.end_of_day()
        self.is_alive()


name = input("Input name:")
nick = Student(name=name)
for i in range(1, 365):
    if nick.alive == False:
        break
    nick.live(i)
    