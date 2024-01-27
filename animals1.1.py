class Animal:
    kind = "bird"
    planet = "earth"
    beak = "has beak"

    def __init__(self, name, color, type):
        self.name = name
        self.color = color
        self.type = type

print(Animal.kind, Animal.planet, Animal.beak)
an = Animal(name="kiwi", color="brown", type="chordal")
an1 = Animal(name="pigeon", color="grey", type="columbidae")
an2 = Animal(name="swan", color="white", type="anatidae")

print(f"an {an.name},{an.color},{an.type}")
print(f"an1 {an1.name},{an1.color},{an1.type}")
print(f"an2 {an2.name},{an2.color},{an2.type}")
