import random

class Shape:
    name = "shape"
    color_list = {"Red", "Orange", "Yellow", "Green", "Blue", "Purple", "Pink", "Black", "White", "Gray"}
    color = random.choice(list(color_list))

class Circle(Shape):
    name = "Circle"
    def __init__(self):
        self.radius = random.randint(1, 1000)
        self.area1 = 0

    def circle_area(self):
        self.area1 = 3.14 * self.radius * 2

    def circle_printer(self):
        self.circle_area()
        print(self.name)
        print(self.area1)
        print(self.color)

class Rectangle(Shape):
    name = "Rectangle"

    def __init__(self):
        self.length = random.randint(1, 1000)
        self.width = random.randint(1, 1000)
        self.area2 = 0

    def rectangle_area(self):
        self.area2 = self.length * self.width


    def rectangle_printer(self):
        self.rectangle_area()
        print(self.name)
        print(self.area2)
        print(self.color)


class Triangle(Shape):
    name = "Triangle"

    def __init__(self):
        self.base = random.randint(1, 1000)
        self.lateral_side = random.randint(1 , 1000)
        self.area3 = 0
    def triangle_area(self):
        self.area3 = self.lateral_side * 2 + self.base

    def triangle_printer(self):
        print(self.name)
        print(self.area3)
        print(self.color)


circle1 = Circle()
rectangle1 = Rectangle()
triangle1 = Triangle()

circle1.circle_printer()
rectangle1.rectangle_printer()
triangle1.triangle_printer()






