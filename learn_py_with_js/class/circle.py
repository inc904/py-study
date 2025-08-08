import math


class Circle:
    pi = math.pi
    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def create_circle(cls, radius):
        return Circle(radius)

    def get_area(self):
        return self.pi * self.radius ** 2

    def get_circumference(self):
        return 2 * self.pi * self.radius

    def __str__(self):
        return f'Circle with radius {self.radius}'


circle = Circle(5)
print(circle)
print(circle.get_area())
print(circle.get_circumference())
