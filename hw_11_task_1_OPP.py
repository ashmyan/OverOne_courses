import math


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Circle:

    def __init__(self, point1, r):
        self._r = r
        self._point = point1

    def area(self):
        return math.pi * (self._r ** 2)

    def perimeter(self):
        return 2 * math.pi * self._r


class Triangle:

    def __init__(self, a, b, c):
        def side(dot1, dot2):
            return math.sqrt((dot1.x - dot2.x) ** 2 + (dot1.y - dot2.y) ** 2)

        self._a = a
        self._b = b
        self._c = c
        self._AB = side(self._a, self._b)
        self._BC = side(self._b, self._c)
        self._CA = side(self._c, self._a)

    def area(self):
        polu_perimeter = self.perimeter() / 2
        return math.sqrt(polu_perimeter
                         * (polu_perimeter - self._AB)
                         * (polu_perimeter - self._BC)
                         * (polu_perimeter - self._CA))

    def perimeter(self):
        return self._AB + self._BC + self._CA


class Square:

    def __init__(self, a, b):
        def side(dot1, dot2):
            return math.sqrt((dot1.x - dot2.x) ** 2
                             + (dot1.y - dot2.y) ** 2) / math.sqrt(2)

        self._a = a
        self._b = b
        self._AB = side(self._a, self._b)

    def perimeter(self):
        return self._AB * 4

    def area(self):
        return self._AB ** 2


point1 = Point(5, 5)
point2 = Point(2, 4)
point3 = Point(3, 6)

circle_1 = Circle(point1, 5)
print(circle_1.area())

triangle_1 = Triangle(point1, point2, point3)
print(triangle_1.area())

square_1 = Square(point1, point2)
print(square_1.area())

figures = [circle_1, triangle_1, square_1]
total_area = 0

for figure in figures:
    total_area += figure.area()
print(total_area)
