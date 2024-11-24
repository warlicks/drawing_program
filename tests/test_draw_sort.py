from draw.drawing_program import DrawingProgram
from draw import ShapeFactory


def test_empty_shapes():
    """Test behavior for DrawingProgram with an empty shapes list"""
    d = DrawingProgram()

    d.sort_shapes()

    assert d.shapes == []


def test_sort_same_shapes():
    """Test DrawingProgram() sort_shapes works for same shape but different dimensions"""
    input = [
        ShapeFactory.create_shape("square", length=10),
        ShapeFactory.create_shape("square", length=1),
        ShapeFactory.create_shape("square", length=15),
        ShapeFactory.create_shape("square", length=0.1),
    ]
    expected_out = [
        "Square, area: 0.01, perimeter: 0.40",
        "Square, area: 1.00, perimeter: 4.00",
        "Square, area: 100.00, perimeter: 40.00",
        "Square, area: 225.00, perimeter: 60.00",
    ]

    d = DrawingProgram(input)

    d.sort_shapes()

    sorted_shapes = [x.draw() for x in d.shapes]

    assert sorted_shapes == expected_out


def test_sort_all_different_shapes():
    """Test DrawingProgram() sort_shapes works for different shapes"""
    input = [
        ShapeFactory.create_shape("Triangle", side1=10, side2=10, base=12, height=6),
        ShapeFactory.create_shape("circle", radius=10),
        ShapeFactory.create_shape("square", length=10),
        ShapeFactory.create_shape("reCtangle", length=10, width=20.5),
    ]

    d = DrawingProgram(input)
    d.sort_shapes()
    shorted_shapes = [x.shape_name for x in d.shapes]

    assert shorted_shapes == ["Circle", "Rectangle", "Square", "Triangle"], print(
        f"{shorted_shapes}"
    )


def test_multiple_combos():
    """Test DrawingProgram() sort_shapes works for same shape but different dimensions and different shapes"""
    input = [
        ShapeFactory.create_shape("Triangle", side1=10, side2=10, base=12, height=6),
        ShapeFactory.create_shape("circle", radius=10),
        ShapeFactory.create_shape("square", length=10),
        ShapeFactory.create_shape("reCtangle", length=10, width=20.5),
        ShapeFactory.create_shape("square", length=100),
    ]
    expected_shapes = [
        "Circle",
        "Rectangle",
        "Square",
        "Square",
        "Triangle",
    ]
    d = DrawingProgram(input)
    d.sort_shapes()
    sorted_shape_names = [x.shape_name for x in d.shapes]
    assert sorted_shape_names == expected_shapes
    assert d.shapes[2].area() == 100
    assert d.shapes[3].area() == 10000


def test_single_shape_sort():
    """Test sort_shapes method in DrawingProgram()"""
    d = DrawingProgram()
    d.add_shape(ShapeFactory.create_shape("circle", radius=10))
    pre_sort = d.shapes

    d.sort_shapes()

    assert pre_sort == d.shapes


def test_equal_shapes():
    """Test sort_shapes when two shapes are the same shape and dimension"""
    d = DrawingProgram(
        [
            ShapeFactory.create_shape("square", length=5),
            ShapeFactory.create_shape("square", length=5),
        ]
    )

    pre_sort = d.shapes
    d.sort_shapes()

    assert [x.shape_name for x in d.shapes] == ["Square", "Square"]
    assert [x.area() for x in d.shapes] == [25, 25]
