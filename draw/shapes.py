import abc
from math import pi


class Shape(abc.ABC):

    @property
    @abc.abstractmethod
    def shape_name(self):
        pass

    @abc.abstractmethod
    def area(self):
        pass

    @abc.abstractmethod
    def perimeter(self):
        pass

    def draw(self):
        return self.__str__()

    def __str__(self):
        return f"{self._shape_name}, area: {self.area():.2f}, perimeter: {self.perimeter():.2f}"


class Circle(Shape):
    def __init__(self, radius: int | float):
        self._shape_name = "Circle"
        self.radius = radius

    def shape_name(self) -> str:
        return self._shape_name

    def area(self) -> int | float:
        return pi * self.radius**2

    def circumference(self) -> int | float:
        return 2 * pi * self.radius

    def perimeter(self):
        return self.circumference()
