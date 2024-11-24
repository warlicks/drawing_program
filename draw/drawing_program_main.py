from .drawing_program import DrawingProgram
from shape_factory import ShapeFactory


class DrawingProgramMain(DrawingProgram, ShapeFactory):
    """Create a class called DrawingProgramMain that creates a DrawingProgram,
    adds shapes to it. Sorts the shapes, adds some more shapes, replaces some shapes,
    sorts again. Each step is printed."""

    # create instance of DrawingProgram()
    draw_prog = DrawingProgram()

    # print empty list (nothing to return)
    print(draw_prog)

    draw_prog.add_shape(ShapeFactory.create_shape("square", length=4))
    # print only square
    print(draw_prog)

    draw_prog.add_shape(ShapeFactory.create_shape("circle", radius=2))
    # print square and circle
    print(draw_prog)

    draw_prog.sort_shapes()
    # print reordered shapes: circle then square
    print(draw_prog)

    draw_prog.set_shape(
        index=0,
        shape=ShapeFactory.create_shape(
            "triangle", side1=10, side2=10, base=12, height=6
        ),
    )
    # print shapes after replacement: triangle then square
    print(draw_prog)
