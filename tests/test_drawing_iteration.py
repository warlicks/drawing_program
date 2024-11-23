from operator import length_hint
import pytest
from draw.drawing_program import DrawingProgram
from draw import ShapeFactory
from draw.shapes import Circle


@pytest.fixture(scope="module")
def drawing_program():
    """Creates an empty DrawingProgram Instance for tests"""
    return DrawingProgram()


@pytest.fixture
def drawing_program2(scope="module"):
    """Creates a drawing instances with four shapes for tests"""
    shape_list = [
        ShapeFactory.create_shape("circle", radius=10),
        ShapeFactory.create_shape("square", length=10),
        ShapeFactory.create_shape("rectangle", length=10, width=20.5),
        ShapeFactory.create_shape("triangle", side1=10, side2=10, base=12, height=6),
    ]

    return DrawingProgram(shape_list)


@pytest.fixture(scope="module")
def drawing_program2_expected_output():
    """Defines expected output for test_multiple_shapes."""
    msg = """Circle, area: 314.16, perimeter: 62.83\nSquare, area: 100.00, perimeter: 40.00\nRectangle, area: 205.00, perimeter: 61.00\nTriangle, area: 36.00, perimeter: 32.00\n"""
    return msg


# The capsys fixture capture standard out and standard error.
def test_no_shapes(capsys, drawing_program):
    """Test that empty string returned with no shapes in instance"""
    for shape in drawing_program:
        print(shape)
        captured = capsys.readouterr()

        assert captured.out == ""


def test_with_single_shape(capsys, drawing_program):
    """Test that iterator works with single item in instance"""
    drawing_program.add_shape(ShapeFactory.create_shape("circle", radius=10))

    for shape in drawing_program:
        print(shape)

    captured = capsys.readouterr()

    assert captured.out == "Circle, area: 314.16, perimeter: 62.83\n"


def test_multiple_shapes(capsys, drawing_program2, drawing_program2_expected_output):
    """Test that iterator works with multiple items."""
    for shape in drawing_program2:
        print(shape)

    captured = capsys.readouterr()

    assert captured.out == drawing_program2_expected_output


def test_string_rep(capsys, drawing_program2, drawing_program2_expected_output):
    """Test the string representation of a DrawingProgram instance

    Tested this here since it should generate the same output as the iterator.
    """
    print(drawing_program2)
    captured = capsys.readouterr()
    assert captured.out == drawing_program2_expected_output


def test_print_shapes(capsys):
    """Creates a drawing instances with four shapes for tests"""
    shape_list = [
        ShapeFactory.create_shape("circle", radius=10),
        ShapeFactory.create_shape("square", length=10),
        ShapeFactory.create_shape("rectangle", length=10, width=20.5),
        ShapeFactory.create_shape("triangle", side1=10, side2=10, base=12, height=6),
        ShapeFactory.create_shape("Circle", radius=1),
    ]

    d = DrawingProgram(shape_list)
    d.print_shapes(Circle)
    captured = capsys.readouterr()

    assert (
        captured.out
        == """Circle, area: 314.16, perimeter: 62.83\nCircle, area: 3.14, perimeter: 6.28"""
    )


def test_empty_print():
    d2 = DrawingProgram()

    with pytest.raises(ValueError):
        d2.print_shapes(Circle)
