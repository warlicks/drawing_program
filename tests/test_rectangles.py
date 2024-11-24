import pytest
from draw.shapes import Rectangle, Shape


@pytest.fixture
def rectangle() -> Rectangle:
    """Creates rectangle instance for use in tests."""
    c = Rectangle(10, 20.5)
    return c


def test_subclass(rectangle):
    """Check that we have a valid Shape subclass."""
    assert isinstance(rectangle, Shape)


def test_rectangle_property(rectangle):
    """Test that shape_name proprty returns the correct name"""
    assert rectangle.shape_name == "Rectangle"


def test_draw_rectangle(rectangle):
    """Test that .draw method outputs as expected"""
    assert rectangle.draw() == "Rectangle, area: 205.00, perimeter: 61.00"


def test_print_rectangle(rectangle):
    """Test that we have correctly implemented string representation."""
    assert str(rectangle) == "Rectangle, area: 205.00, perimeter: 61.00"


def test_rectangle_area(rectangle):
    """Test that we get the correct area calculation"""
    assert rectangle.area() == 205


def test_rectangle_perimiter(rectangle):
    """Test that we get correct perimeter calculation"""
    assert rectangle.perimeter() == 61
