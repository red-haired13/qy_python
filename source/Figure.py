import math
from math import sqrt


class Figure:

    def __init__(self, name, angles):
        self.name = name
        self.angles = angles


class Triangle(Figure):
    def __init__(self, name, angles, sideA, sideB, sideC):
        Figure.__init__(self, name, angles)
        self.sideA = sideA
        self.sideB = sideB
        self.sideC = sideC

    def calculate_perimeter(self):
        p = (self.sideA + self.sideB + self.sideC)
        return p

    def calculate_area(self, p):
        p = p / 2
        s = sqrt(p * (p - self.sideA) * (p - self.sideB) * (p - self.sideC))
        return s

    def add_area(self, s, figure):
        if isinstance(figure, (Rectangle, Square, Circle)):
            s = s + figure.calculate_area()
            return s
        elif not isinstance(figure, (Rectangle, Square, Circle)):
            return "This is not a figure"


class Rectangle(Figure):
    def __init__(self, name, angles, sideA, sideB):
        Figure.__init__(self, name, angles)
        self.sideA = sideA
        self.sideB = sideB

    def calculate_area(self):
        s = self.sideA * self.sideB
        return s

    def calculate_perimeter(self):
        p = (self.sideA + self.sideB) * 2
        return p

    def add_area(self, s, figure):
        if isinstance(figure, (Triangle, Square, Circle)):
            s = s + figure.calculate_area()
            return s
        elif not isinstance(figure, (Triangle, Square, Circle)):
            return "This is not a figure"


class Square(Figure):
    def __init__(self, name, angles, sideA):
        Figure.__init__(self, name, angles)
        self.sideA = sideA

    def calculate_area(self):
        s = self.sideA * self.sideA
        return s

    def calculate_perimeter(self):
        p = self.sideA * 4
        return p

    def add_area(self, s, figure):
        if isinstance(figure, (Triangle, Rectangle, Circle)):
            s = s + figure.calculate_area()
            return s
        elif not isinstance(figure, (Triangle, Rectangle, Circle)):
            return "This is not a figure"


class Circle(Figure):
    def __init__(self, name, angles, rad):
        Figure.__init__(self, name, angles)
        self.rad = rad

    def calculate_area(self):
        s = math.pi * (self.rad ** 2)
        return s

    def calculate_perimeter(self):
        p = 2 * math.pi * self.rad
        return p

    def add_area(self, s, figure):
        if isinstance(figure, (Triangle, Rectangle, Square)):
            s = s + figure.calculate_area()
            return s
        elif not isinstance(figure, (Triangle, Rectangle, Square)):
            return "This is not a figure"


# tri = Triangle('Triangle', 3, 5, 5, 6)
# r = tri.calculate_perimeter()
# t = tri.calculate_area(r)
# fig = Square("Square", 2, 4)
# tri.add_area(t, fig)

#rec = Rectangle('Rectangle', 2, 4, 5)
#r = rec.calculate_perimeter()
#t = rec.calculate_area()

#squ = Square('Square', 2, 2)
#r = squ.calculate_perimeter()
#t = squ.calculate_area()

cir = Circle('Circle', 2, 5)
r = cir.calculate_perimeter()
t = cir.calculate_area()
