import abc
from math import pi


class Shape(abc.ABC):
    """Abstract Base Class For Shapes

    The abstract bases class defines the interface that other classes need to
    follow. Classes that inherit from Shape must implement an area and perimeter
    method. They must also implement a shape_name property.

    The draw method is not defined as an abstract method. An can be used by all
    children to print the shape name, it's area and perimeter
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

    def __str__(self):
        return f"{self.shape_name}, area: {self.area():.2f}, perimeter: {self.perimeter():.2f}"


class Circle(Shape):
    def __init__(self, radius: int | float) -> None:
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

    def area(self) -> int | float:
        """Computes the Area of the Circle


        Returns:
            int | float: The area of the circle.
        """
        return pi * self.radius**2

    def circumference(self) -> int | float:
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
    def __init__(self, length: int | float) -> None:
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

    def area(self) -> int | float:
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


class Rectangle(Square):
    def __init__(self, length: int | float, width: int | float) -> None:
        """Creates an instance of the Rectangle Class

        Since a square is just a special case of a rectangle rectangle class
        inherits from the square class. The only significant change is that you
        must specify the length and the width of the rectangle when creating an
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
