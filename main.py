import random

class Numbers:
    _a = random.randint(1,1000)
    _b = random.randint(1,1000)
    
    cube = random.randint(1,4)
    if cube == 1:
        print(_a+_b)
    if cube == 2:
        print(_a-_b)
    if cube == 3:
        print(_a*_b)
    if cube == 4:
        print(_a/_b)
