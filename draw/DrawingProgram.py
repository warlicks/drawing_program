# Your team will create a program that has a class that holds a list/collection of shapes. This class will
# be named DrawingProgram. Here are the attributes (data) and behaviors (methods) of this class:
from shape_factory import ShapeFactory


class DrawingProgram(ShapeFactory):
    # For the intents and purposes of this assignment, all shapes should be created via ShapeFactory.
    #     Thus any adding of shapes to your DrawingProgram class object must be done through ShapeFactory.
    #     This may seem cumbersome, but the point is to leave object creation to a single class.
    #         It encapsulates how to create the objects you need.
    #  ^^^ I think this means we pass in ShapeFactory into DrawingProgram instead of the shapes themselves?

    def __init__(self, Shapes = None):
        if Shapes is None or isinstance(Shapes, list):
            self.Shapes = Shapes
        else:
            Exception(f"Shapes: {Shapes} is not None or a list.")

    def add_shape(self, Shape):
        self.Shapes.append(Shape)

    def remove_shape(self, Shape):
        """remove shape that exists in the DrawingProgram.Shapes list, else throw an exception"""
        shape_rm_count = self.Shapes.count(Shape)
        if Shape in self.Shapes:
            self.Shapes.remove(Shape)
        else:
            raise Exception(f'{Shape} not in {self.Shapes}')

        print(f"{shape_rm_count} number of occurrences removed from shape list.")
        return shape_rm_count

    def print_shapes(self, Shape):
        """prints all shapes that match the type of the shape passed in"""

    def sort_shapes(self):
        """sorts the list/collection of shapes -- you must use a sort
        that runs in O(nlogn) for its worst case. shapes will be sorted
        first by name, then by area if names are same"""
        # Sean's question: can we use preprogrammed sort_shapes(): "sorts the list/collection of shapes --
        #  ^^ concat name and area and put together to do it

    def __str__(self):
        """returns a string representation of each of the shapes --
        each shape will be separated from others by a newline (\n)"""

    def get_shape(self, index):
        """returns the shape at the specified index"""

    def set_shape(self, index, Shape):
        """replaces the shape at the specified index any other
        behaviors you feel are necessary for the class"""


class DrawingProgramIterator:
    """DrawingProgramIterator provides the ability to iterate
    across the collection of shapes in DrawingProgram using a for loop."""
    # See notes/slides on Iterator and
    # book chapter "The Iterator Pattern" and the section "The Iterator Protocol"
    # Sean's question: (why not build it into the class?)


class DrawingProgramMain(DrawingProgram):
    #     Create a class called DrawingProgramMain that creates a DrawingProgram,
    #     adds shapes to it. Sorts the shapes, adds some more shapes, replaces some shapes,
    #     sorts again. With each thing done be sure and include print statements to show what was done.

