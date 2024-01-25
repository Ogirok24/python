class Animal:
    kind = "bird"
    planet = "earth"
    beak = "has beak"

    def __init__(self, name, color):
        self.name = name
        self.color = color

print(Animal.kind, Animal.planet, Animal.beak)
an = Animal(name="kiwi", color="brown")
an1 = Animal(name="pigeon", color="grey")
an2 = Animal(name="swan", color="white")

print(f"Name an {an.name},{an.color}")
print(f"Name an1 {an1.name},{an1.color}")
print(f"Name an2 {an2.name},{an2.color}")