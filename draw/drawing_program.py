# Your team will create a program that has a class that holds a list/collection of shapes. This class will
# be named DrawingProgram. Here are the attributes (data) and behaviors (methods) of this class:


class DrawingProgram:
    # For the intents and purposes of this assignment, all shapes should be created via ShapeFactory.
    #     Thus any adding of shapes to your DrawingProgram class object must be done through ShapeFactory.
    #     This may seem cumbersome, but the point is to leave object creation to a single class.
    #         It encapsulates how to create the objects you need.
    #  ^^^ I think this means we pass in ShapeFactory into DrawingProgram instead of the shapes themselves?

    def __init__(self, shapes: list = []):
        self.shapes = shapes

    def add_shape(self, shape):
        self.shapes.append(shape)

    def remove_shape(self, shape):
        """remove shape that exists in the DrawingProgram.Shapes list, else throw an exception"""
        shape_rm_count = self.shapes.count(shape)
        if shape in self.shapes:
            self.Shapes.remove(shape)
        else:
            raise Exception(f"{shape} not in {self.shapes}")

        print(f"{shape_rm_count} number of occurrences removed from shape list.")
        return shape_rm_count

    def print_shapes(self, shape):
        """prints all shapes that match the type of the shape passed in.
        throw exception if shape is not in ShapeFactory shapes."""
        if shape not in ShapeFactory.shape_dict():
            Exception(f"{shape} is not a shape in ShapeFactory.")

        matched_shapes = []
        for each_shape in self.shapes:
            if isinstance(shape, each_shape):
                matched_shapes.append(each_shape)

        return matched_shapes

    def sort_shapes(self):
        """sorts the list/collection of shapes -- you must use a sort
        that runs in O(nlogn) for its worst case. shapes will be sorted
        first by name, then by area if names are same"""
        # Sean's question: can we use preprogrammed sort_shapes(): "sorts the list/collection of shapes --
        #  ^^ concat name and area and put together to do it

    def __iter__(self):
        """Internal method enabling the iteration through the collection of shapes"""
        return DrawingProgramIterator(self.shapes)

    def __str__(self):
        """Returns a string representation of each of the shapes
        each shape will be separated from others by a newline (\n)"""
        msg = "\n".join([str(x) for x in self.shapes])

        return msg

    def get_shape(self, index):
        """returns the shape at the specified index"""

    def set_shape(self, index, shape):
        """replaces the shape at the specified index any other
        behaviors you feel are necessary for the class"""


class DrawingProgramIterator:
    """Provides the ability to iterate across the collection of shapes in DrawingProgram


    DrawingProgramIterator is called internally by the __iter__ method of
    DrawingProgram. This allows iteration of over the collection of shapes in a
    given DrawingProgram instance. It is implemented this way to demonstrate the
    Iterator design pattern.

    The given that it illustrates the design patter implementation is not
    specific to the DrawingProgram and could be used to iterate over
    lists of other object types, but this is overkill since lists are
    already iterable.
    """

    def __init__(self, shapes: list) -> None:
        """Creates an DrawingProgramIterator
        Args:
            shapes (list): A list of items to be iterated over.
        """
        self.shapes = shapes
        # Note to self, if you set index to zero in the __next__ you get an infinite loop.
        self.index = 0

    def __iter__(self):
        """Internal method that creates an iterator callable by next"""
        return self

    def __next__(self):
        """Internal method responsible for returning next element of the iteration."""
        while self.index <= (len(self.shapes) - 1):
            current_value = self.shapes[self.index]
            self.index += 1
            return current_value
        else:
            raise StopIteration


class DrawingProgramMain(DrawingProgram):
    #     Create a class called DrawingProgramMain that creates a DrawingProgram,
    #     adds shapes to it. Sorts the shapes, adds some more shapes, replaces some shapes,
    #     sorts again. With each thing done be sure and include print statements to show what was done.

    pass
