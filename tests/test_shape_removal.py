import pytest
from draw.drawing_program import DrawingProgram
from draw import ShapeFactory
from draw.shapes import Rectangle, Square, Circle, Triangle


@pytest.fixture
def draw():
    """create a DrawingProgram() object to be used in tests"""
    d = DrawingProgram(
        [
            ShapeFactory.create_shape("circle", radius=10),
            ShapeFactory.create_shape("circle", radius=20),
            ShapeFactory.create_shape("rectangle", length=10, width=3),
        ]
    )

    return d


def test_no_square(draw):
    """Test exception is thrown when there is no square to remove"""
    with pytest.raises(Exception):
        draw.remove_shape(Square)


def test_remove_circle(draw):
    """Test how many circles are removed from shapes and number of remaining"""
    removed = draw.remove_shape(Circle)

    assert removed == 2
    assert len(draw.shapes) == 1


def test_sequential_remove(draw):
    """Test when rectangle is removed first and then circle is removed"""
    removed = draw.remove_shape(Rectangle)

    assert removed == 1

    removed2 = draw.remove_shape(Circle)
    assert removed2 == 2
    assert len(draw.shapes) == 0


def test_empty_remove():
    """Test exception is thrown when trying to remove a shape from an empty list"""
    d = DrawingProgram()
    with pytest.raises(Exception):
        d.remove_shape(Triangle)
