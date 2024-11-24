import pytest
from draw.shapes import Circle, Shape


@pytest.fixture
def circle() -> Circle:
    """Creates Circle instance for use in tests."""

    c = Circle(10)

    return c


def test_subclass(circle):
    """Check that we have a valid Shape subclass."""
    assert isinstance(circle, Shape)


def test_circle_property(circle):
    """Test that shape_name proprty returns the correct name"""
    assert circle.shape_name == "Circle"


def test_draw_circle(circle):
    """Test that .draw method outputs as expected"""
    assert circle.draw() == "Circle, area: 314.16, perimeter: 62.83"


def test_print_circle(circle):
    """Test that we have correctly implemented string representation."""
    assert str(circle) == "Circle, area: 314.16, perimeter: 62.83"


def test_circle_area(circle):
    """Test that we get the correct area calculation"""
    assert circle.area() == pytest.approx(314.16, rel=0.01)


def test_circle_perimeter(circle):
    """Test that we get correct perimeter calculation"""
    assert circle.perimeter() == pytest.approx(62.83, rel=0.02)
