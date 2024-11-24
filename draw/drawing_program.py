# Your team will create a program that has a class that holds a list/collection of shapes. This class will
# be named DrawingProgram. Here are the attributes (data) and behaviors (methods) of this class:
from draw.shapes import Shape


class DrawingProgram:
    # For the intents and purposes of this assignment, all shapes should be created via ShapeFactory.
    #     Thus any adding of shapes to your DrawingProgram class object must be done through ShapeFactory.
    #     This may seem cumbersome, but the point is to leave object creation to a single class.
    #         It encapsulates how to create the objects you need.
    #  ^^^ I think this means we pass in ShapeFactory into DrawingProgram instead of the shapes themselves?

    def __init__(self, shapes: list = []):
        """Creates a DrawingProgram Instance

        Args:
            shapes (list, optional): A collection of Shapes in a list.
              Defaults to an empty list.
        """
        self.shapes = shapes

    def add_shape(self, shape: Shape):
        """Add a shape to the collection of shapes

        Args:
            shape (Shape): The shape to add to the collection.
        """

        self.shapes.append(shape)

    def remove_shape(self, shape: Shape) -> int:
        """Removes all instances of a shape from the collection of shapes


        Args:
            shape (Shape): The shape you want to remove from the collection of shapes.

        Raises:
            Exception: Indicates that there were no itmes of the given shape in the
              collection of shapes

        Returns:
            int: The number of items removed from the collection of shapes.
        """
        start_length = len(self.shapes)

        i = 0
        while i < len(self.shapes):
            if isinstance(self.shapes[i], shape):
                del self.shapes[i]
            else:
                i += 1

        end_length = len(self.shapes)
        shape_rm_count = start_length - end_length

        if shape_rm_count == 0:
            raise Exception(f"{shape} not present")

        print(f"{shape_rm_count} number of {print(shape)} removed from shape list.")
        return shape_rm_count

    def print_shapes(self, shape: Shape):
        """Prints all shapes that match the type of the shape

        Args:
            shape (Shape): The type of shape to print information about.

        Raises:
            ValueError: If there are no intances of the given shape in the collection
              of shapes.

        Returns:
            Prints shape information
        """

        matched_shapes = []
        for each_shape in self.shapes:
            if isinstance(each_shape, shape):
                matched_shapes.append(each_shape)
        if len(matched_shapes) == 0:
            raise ValueError(f"There is no {shape} in the shape collection")
        else:
            for x in matched_shapes:
                print(x)

    def sort_shapes(self) -> None:
        """Sorts the list/collection of shapes

        You must use a sort that runs in O(nlogn) for its worst case. Shapes will be sorted
        first by name, then by area if names are same. The sort happens in place.

        """
        self.shapes = self._merge_sort(self.shapes)

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

    def _merge_sort(self, data: list):
        """Internal Method for sorting shapes."""
        # Define the base case:
        if len(data) <= 1:
            return data

        # Recursively split the list
        middle = len(data) // 2
        left = data[:middle]
        right = data[middle:]

        s_left = self._merge_sort(left)
        s_right = self._merge_sort(right)

        return self._merge(s_left, s_right)

    def _merge(self, left, right):
        """Internal method that handles the merge portion of merge sort for sorting
        shapes.
        """
        result_storage = []
        # Check for shape name differences and sort by name
        while left and right:
            if left[0].shape_name < right[0].shape_name:
                result_storage.append(left[0])
                left.pop(0)
            elif left[0].shape_name > right[0].shape_name:
                result_storage.append(right[0])
                right.pop(0)
            # If the names are the same we make comparison to the shape area.
            else:
                if left[0].area() < right[0].area():
                    result_storage.append(left[0])
                    left.pop(0)
                else:
                    result_storage.append(right[0])
                    right.pop(0)

        if left:
            result_storage += left
        if right:
            result_storage += right

        return result_storage


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
