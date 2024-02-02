class Human:
    def __init__(self, name="Human"):
        self.name = name
class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passangers = []
    def add_passenger(self, human):
        self.passangers.append(human)
    def print_passengers_names(self):
        if  self.passangers != []:
            print(f"Names of {self.brand} passengers")
            for passenger in self.passangers:
                print((passenger.name))
        else:
            print(f"There are no passangers in {self.brand}")

nick = Human("Nick")
kate = Human("Kate")
car = Auto("Volvo")
car.add_passenger(nick)
car.print_passengers_names()
car.add_passenger(kate)
car.print_passengers_names()
