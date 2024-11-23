import pytest
from draw.drawing_program import DrawingProgram
from draw import ShapeFactory
from draw.shapes import Rectangle, Square, Circle, Triangle


@pytest.fixture
def draw():
    d = DrawingProgram(
        [
            ShapeFactory.create_shape("circle", radius=10),
            ShapeFactory.create_shape("circle", radius=20),
            ShapeFactory.create_shape("rectangle", length=10, width=3),
        ]
    )

    return d


def test_no_square(draw):

    with pytest.raises(Exception):
        draw.remove_shape(Square)


def test_remove_circle(draw):
    removed = draw.remove_shape(Circle)

    assert removed == 2
    assert len(draw.shapes) == 1


def test_sequential_remove(draw):
    removed = draw.remove_shape(Rectangle)

    assert removed == 1

    removed2 = draw.remove_shape(Circle)
    assert removed2 == 2
    assert len(draw.shapes) == 0


def test_empyt_remove():
    d = DrawingProgram()
    with pytest.raises(Exception):
        d.remove_shape(Triangle)
