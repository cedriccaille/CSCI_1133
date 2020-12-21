class Quadrilateral:
    def __init__(self,a,b,c,d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    def perimeter(self):
        return self.a + self.b + self.c + self.d
    def area(self):
        print("Not enough information")

#Problem A -- Rectangle Class
class Rectangle(Quadrilateral):
    def __init__(self, width, length):
        Quadrilateral.__init__(self, width, length, width, length)
    def area(self):
        return self.a * self.b

#Problem B -- Rhombus Class
import math
class Rhombus(Quadrilateral):
    def __init__(self, side, angle):
        Quadrilateral.__init__(self, side, side, side, side)
        self.angle = angle
    def area(self):
        return self.a * self.b * math.sin(self.angle)

#Problem C -- Polymorphism
def avg_perimeter(quad_lst):
    total_perimeter = 0
    divisor = len(quad_lst)
    for shape in quad_lst:
        total_perimeter += shape.perimeter()
    return total_perimeter / divisor
