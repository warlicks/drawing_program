import pytest
from draw import shape_factory
from draw.shape_factory import ShapeFactory
from draw.shapes import Circle, Rectangle, Square, Triangle


def test_circle_create():
    """Test that we get a working circle instance from the shape factory.
    I used the same input values as the test for the Ciricle class for consistency
    """
    c = ShapeFactory.create_shape("circle", radius=10)
    assert isinstance(c, Circle)
    assert c.shape_name == "Circle"
    assert c.area() == pytest.approx(314.16, rel=0.01)


def test_square_create():
    """Test that the factory creates a working square instance."""
    s = ShapeFactory.create_shape("square", length=10)
    assert isinstance(s, Square)
    assert s.shape_name == "Square"
    assert s.perimeter() == 40


def test_triangle_create():
    t = ShapeFactory.create_shape("Triangle", side1=10, side2=10, base=12, height=6)
    assert isinstance(t, Triangle)
    assert t.shape_name == "Triangle"
    assert t.perimeter() == 32


def test_rectangle_class():
    """Test that shape factory creates a working rectange instance"""
    r = ShapeFactory.create_shape("reCtangle", length=10, width=20.5)
    assert isinstance(r, Rectangle)
    assert r.shape_name == "Rectangle"
    assert r.area() == 205


def test_error_for_unknown_shape():
    with pytest.raises(AssertionError):
        ShapeFactory.create_shape("Polygon")
