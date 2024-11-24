import abc
from math import pi
from typing import Union


class Shape(abc.ABC):
    """Abstract Base Class For Shapes

    The abstract bases class defines the interface that shapes need to
    follow. Classes that inherit from Shape must implement an area and perimeter
    method. They must also implement a shape_name property.

    The draw method is not defined as an abstract method. An can be used by all
    children to print the shape name, the shape area and the shape perimeter.
    """

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

    def draw(self) -> str:
        """'Draws' the shape.

        When drawing the shape a string with the name of the shape, the
        area and the perimeter are returned. Values are trimmed to the nearest
        hundredth.

        Returns:
            str: String with the format <Shape Name>, area: <shape area>, perimeter: <perimeter>.
        """
        return self.__str__()

    def __str__(self) -> str:
        """Internal Method for string representation of the shape instance

        Returns:
            str: String with the format <Shape Name>, area: <shape area>, perimeter: <perimeter>.
        """
        return f"{self.shape_name}, area: {self.area():.2f}, perimeter: {self.perimeter():.2f}"
        # return f"{self.shape_name}, area: {self.area()}, perimeter: {self.perimeter()}"


class Circle(Shape):
    def __init__(self, radius: Union[int, float]) -> None:
        """Creates an instance of a Circle shape.

        Args:
            radius (int | float): The radius of the circle.
        """
        self._shape_name = "Circle"
        self.radius = radius

    @property
    def shape_name(self) -> str:
        """Returns the shame name for the instances

        Returns:
            str: Circle
        """
        return self._shape_name

    def area(self) -> Union[int, float]:
        """Computes the Area of the Circle


        Returns:
            int | float: The area of the circle.
        """
        return pi * self.radius**2

    def circumference(self) -> Union[int, float]:
        """Computes the (circumference) of the circle

        Returns:
            int | float: : The circle's circumference
        """
        return 2 * pi * self.radius

    def perimeter(self):
        """Computes the perimeter (circumference) of the circle

        Returns:
            int | float: : The circle's circumference
        """
        return self.circumference()


class Square(Shape):
    def __init__(self, length: Union[int, float]) -> None:
        """Creates an instance of a Square shape.

        Since all four sides of a square are equal length you only need to specify
        the dimensions of one side.

        Args:
            length (int | float): The length of the squares sides.
        """
        self._shape_name = "Square"
        self.length = length
        self.width = length

    @property
    def shape_name(self) -> str:
        """Returns the shape name for the instances

        Returns:
            str: Square
        """
        return self._shape_name

    def area(self) -> Union[int, float]:
        """Computes the Area of the Square

        Returns:
            int | float: The area of the square.
        """
        return self.length * self.width

    def perimeter(self):
        """Computes the perimeter  of the Square

        Returns:
            int | float: : The square's perimeter
        """
        return self.length * 2 + self.width * 2


class Rectangle(Shape):
    def __init__(self, length: Union[int, float], width: Union[int, float]) -> None:
        """Creates an instance of the Rectangle Class

        Since a square is just a special case of a rectangle, rectangle class
        inherits from the square class. The only significant change is that you
        must specify the length and width of the rectangle when creating an
        instance.

        Args:
            length (int | float): The length of the rectangle.
            width (int | float): The width of the rectangle.
        """
        self._shape_name = "Rectangle"
        self.length = length
        self.width = width

    @property
    def shape_name(self) -> str:
        """Returns the shape name for the instances

        Returns:
            str: Square
        """
        return self._shape_name

    def area(self) -> Union[int, float]:
        """Computes the Area of the Rectangle

        Returns:
            int | float: The area of the Rectangle.
        """
        return self.length * self.width

    def perimeter(self):
        """Computes the perimeter  of the Rectangle

        Returns:
            int | float: : The square's Rectangle
        """
        return self.length * 2 + self.width * 2


class Triangle(Shape):
    def __init__(
        self,
        side1: Union[int, float],
        side2: Union[int, float],
        base: Union[int, float],
        height: Union[int, float],
    ) -> None:
        """Creates an instance of the triangle class

        Args:
            side1 (int | float): The length of a side of the triangle
            side2 (int | float): The length of a side of the triangle
            base (int | float): The length of the base of the triangle
            height (int | float): The height of the triangle.
        """
        self._shape_name = "Triangle"
        self.side1 = side1
        self.side2 = side2
        self.base = base
        self.height = height

    @property
    def shape_name(self):
        """Returns the shape name for the instances

        Returns:
            str: Triangle
        """
        return self._shape_name

    def area(self):
        """Computes the Area of the Triangle

        Returns:
            int | float: The area of the triangle.
        """
        return 0.5 * self.base * self.height

    def perimeter(self):
        """Computes the Area of the Triangle

        Returns:
            int | float: The area of the triangle.
        """
        return self.side1 + self.side2 + self.base
