import pytest
from draw.shapes import Square, Shape


@pytest.fixture
def square() -> Square:
    """Creates square instance for use in tests."""

    c = Square(10)

    return c


def test_subclass(square):
    """Check that we have a valid Shape subclass."""
    assert isinstance(square, Shape)


def test_square_property(square):
    """Test that shape_name proprty returns the correct name"""
    assert square.shape_name == "Square"


def test_draw_square(square):
    """Test that .draw method outputs as expected"""
    assert square.draw() == "Square, area: 100.00, perimeter: 40.00"


def test_print_square(square):
    """Test that we have correctly implemented string representation."""
    assert str(square) == "Square, area: 100.00, perimeter: 40.00"


def test_square_area(square):
    """Test that we get the correct area calculation"""
    assert square.area() == 100


def test_square_perimeter(square):
    """Test that we get correct perimeter calculation"""
    assert square.perimeter() == 40
