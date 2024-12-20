import pytest
from draw.drawing_program import DrawingProgram
from draw import ShapeFactory
from draw.shapes import Circle, Square, Triangle


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
def test_no_shapes(capsys):
    """Test that empty string returned with no shapes in instance"""
    d = DrawingProgram()
    for shape in d:
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
        == """Circle, area: 314.16, perimeter: 62.83\nCircle, area: 3.14, perimeter: 6.28\n"""
    )


def test_remove_with_single_shape(drawing_program):
    """Test remove_shape returns parameter with the number of that shape that was removed"""
    drawing_program.add_shape(ShapeFactory.create_shape("circle", radius=10))
    drawing_program.add_shape(ShapeFactory.create_shape("circle", radius=10))

    how_many_rm = drawing_program.remove_shape(Circle)

    assert how_many_rm == 2


def test_remove_with_single_shape(drawing_program):
    """Test remove_shape return when shape to remove isn't in drawing_program"""
    drawing_program.add_shape(ShapeFactory.create_shape("circle", radius=10))
    drawing_program.add_shape(ShapeFactory.create_shape("circle", radius=10))

    with pytest.raises(Exception):
        drawing_program.remove_shape(Square)


def test_sort_shapes(capsys):
    """Test sort_shapes sorts the shapes in DrawingProgram()"""
    shape_list = [
        ShapeFactory.create_shape("circle", radius=10),
        ShapeFactory.create_shape("square", length=10),
        ShapeFactory.create_shape("rectangle", length=10, width=20.5),
        ShapeFactory.create_shape("triangle", side1=10, side2=10, base=12, height=6),
        ShapeFactory.create_shape("Circle", radius=1),
    ]

    d = DrawingProgram(shape_list)
    d.sort_shapes()
    print(d)
    captured = capsys.readouterr()

    assert (
        captured.out
        == """Circle, area: 3.14, perimeter: 6.28\nCircle, area: 314.16, perimeter: 62.83\nRectangle, area: 205.00, perimeter: 61.00\nSquare, area: 100.00, perimeter: 40.00\nTriangle, area: 36.00, perimeter: 32.00\n"""
    )


def test_get_shape():
    """Test sort_shapes sorts the shapes in DrawingProgram()"""
    shape_list = [
        ShapeFactory.create_shape("circle", radius=10),
        ShapeFactory.create_shape("square", length=10),
        ShapeFactory.create_shape("rectangle", length=10, width=20.5),
        ShapeFactory.create_shape("triangle", side1=10, side2=10, base=12, height=6),
        ShapeFactory.create_shape("Circle", radius=1),
    ]

    d = DrawingProgram(shape_list)
    index_shape = d.get_shape(1)

    assert index_shape == "Square"


def test_set_shape():
    """Test sort_shapes sorts the shapes in DrawingProgram()"""
    shape_list = [
        ShapeFactory.create_shape("circle", radius=10),
        ShapeFactory.create_shape("square", length=10),
        ShapeFactory.create_shape("rectangle", length=10, width=20.5),
        ShapeFactory.create_shape("triangle", side1=10, side2=10, base=12, height=6),
        ShapeFactory.create_shape("Circle", radius=1),
    ]

    d = DrawingProgram(shape_list)
    d.set_shape(index=1, shape=ShapeFactory.create_shape("Circle", radius=1))

    assert d.shapes[1].shape_name == "Circle"
    assert d.shapes[1].area() == pytest.approx(3.14, rel=0.01)


def test_DrawingProgramIterator(capsys):
    """Test DrawingProgramIterator outputs expected shapes"""
    drawing_program = DrawingProgram()

    for shape in drawing_program:
        print(shape)

    captured = capsys.readouterr()

    assert captured.out == """"""


def test_empty_print():
    """Test empty DrawingProgram raises a value error when trying to print"""
    d2 = DrawingProgram()

    with pytest.raises(ValueError):
        d2.print_shapes(Circle)
