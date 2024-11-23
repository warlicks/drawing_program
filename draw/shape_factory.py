from .shapes import Circle, Square, Rectangle, Triangle


class ShapeFactory:
    """A "factory class" for creating members of the shape class.

    There is only one method for the class create_shape. This method simply wraps the
    creation of a Shape subclass based on the shape name provided. This approach makes
    it easy to add addtional shapes to the factory when a new Shape subclass is created.

    Raises:
        AssertionError: Assertion error is raised if an invalid shape name is provied.

    Returns:
        Shape: A Shape subclass instance appropraite to the shape name provided.
    """

    @staticmethod
    def create_shape(shape_name: str, **kwargs) -> "Shape":
        """Creates the desired shape

        Arguments for desired shape should be passed as **kwargs. See the desired shape
        for details.

        Args:
            shape_name (str): Indicates the shape that should be created by the factory.
              The name of the shape should be provided in lower case characters. Valid
              shape names include 'circle', 'square', 'rectangle' and 'triangel'.



        Raises:
            AssertionError: Assertion error is raised if an invalid shape name is provied.

        Returns:
            Shape: A Shape subclass instance appropraite to the shape name provided.

        """
        if shape_name.lower() == "circle":
            return Circle(**kwargs)
        elif shape_name.lower() == "square":
            return Square(**kwargs)
        elif shape_name.lower() == "rectangle":
            return Rectangle(**kwargs)
        elif shape_name.lower() == "triangle":
            return Triangle(**kwargs)
        else:
            raise AssertionError("Shape Name is Not a Valid Shape Name")
