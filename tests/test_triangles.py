import pytest
from draw.shapes import Triangle, Shape


@pytest.fixture
def triangle() -> Triangle:
    """Creates triangle instance for use in tests."""

    c = Triangle(10, 10, 12, 6)

    return c


def test_subclass(triangle):
    """Check that we have a valid Shape subclass."""
    assert isinstance(triangle, Shape)


def test_triangle_property(triangle):
    """Test that shape_name proprty returns the correct name"""
    assert triangle.shape_name == "Triangle"


def test_draw_triangle(triangle):
    """Test that .draw method outputs as expected"""
    assert triangle.draw() == "Triangle, area: 36.00, perimeter: 32.00"


def test_print_triangle(triangle):
    """Test that we have correctly implemented string representation."""

    assert str(triangle) == "Triangle, area: 36.00, perimeter: 32.00"


def test_triangle_area(triangle):
    """Test that we get the correct area calculation"""
    assert triangle.area() == 36


def test_triangle_perimeter(triangle):
    """Test that we get correct perimeter calculation"""
    assert triangle.perimeter() == 32
