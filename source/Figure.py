import math
from math import sqrt


class Figure:

    def __init__(self, name, angles):
        self.name = name
        self.angles = angles
        print(f"My name's {self.name}")


class Triangle(Figure):

    def calculate_perimeter(self, sideA=2, sideB=2, sideC=3):
        p = (sideA + sideB + sideC)
        print(f"Perimeter : {p}")

    def calculate_area(self, sideA=2, sideB=2, sideC=1.5):
        p = (sideA + sideB + sideC) / 2
        s = sqrt(p * (p - sideA) * (p - sideB) * (p - sideC))
        print(f"Area : {s}")
        return s

    def add_area(self, s, figure):
        if isinstance(figure, (Rectangle, Square, Circle)):
            s = s + figure.calculate_area()
            print(f"All area : {s}")
        elif not isinstance(figure, (Rectangle, Square, Circle)):
            print("This is not a figure")


class Rectangle(Figure):
    def calculate_area(self, sideA=5, sideB=8):
        s = sideA * sideB
        print(f"Area : {s}")
        return s

    def calculate_perimeter(self, sideA=5, sideB=8):
        p = (sideA + sideB) * 2
        print(f"Perimeter : {p}")

    def add_area(self, s, figure):
        if isinstance(figure, (Triangle, Square, Circle)):
            s = s + figure.calculate_area()
            print(f"All area : {s}")
        elif not isinstance(figure, (Triangle, Square, Circle)):
            print("This is not a figure")


class Square(Figure):
    def calculate_area(self, sideA=5):
        s = sideA * sideA
        print(f"Area : {s}")
        return s

    def calculate_perimeter(self, sideA=5):
        p = sideA * 4
        print(f"Perimeter : {p}")

    def add_area(self, s, figure):
        if isinstance(figure, (Triangle, Rectangle, Circle)):
            s = s + figure.calculate_area()
            print(f"All area : {s}")
        elif not isinstance(figure, (Triangle, Rectangle, Circle)):
            print("This is not a figure")


class Circle(Figure):

    def calculate_area(self, rad=5):
        s = math.pi * (rad ** 2)
        print(f"Area : {s}")
        return s

    def calculate_perimeter(self, rad=5):
        p = 2 * math.pi * rad
        print(f"Perimeter : {p}")

    def add_area(self, s, figure):
        if isinstance(figure, (Triangle, Rectangle, Square)):
            s = s + figure.calculate_area()
            print(f"All area : {s}")
        elif not isinstance(figure, (Triangle, Rectangle, Square)):
            print("This is not a figure")


#tri = Triangle('Triangle', 3)
#s = tri.calculate_area()
#tri.calculate_perimeter()

#figure = Rectangle('Rectangle', 2)
#figure.calculate_area()
#figure.calculate_perimeter()
# figure = 10
#figure = Circle('Circle', 2.5)
#figure.calculate_area()
#figure.calculate_perimeter()
# tri.add_area(s, figure)

#squ = Square("Square", 2)
#squ.calculate_area()
# squ.calculate_perimeter(5)

#cir = Circle('Circle', 2.5)
#cir.calculate_area()
