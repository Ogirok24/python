import random

class Numbers:
    def __init__(self, a, b):
        self.__a = a
        self.__b = b
    def __Operation(self, a, b):
        cube = random.randint(1, 4)
        if cube == 1:
            return self.__a + self.__b
        if cube == 2:
            return self.__a - self.__b
        if cube == 3:
            return self.__a * self.__b
        if cube == 4:
            return self.__a / self.__b

    def Result(self):
        return self.__Operation(a , b)



a = random.randint(1, 1000)
b = random.randint(1, 1000)
rand = Numbers(a, b)
print(rand.Result())








