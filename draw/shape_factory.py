from shapes import Circle, Square, Rectangle, Triangle

# create_shape(shape name, shape data): creates a shape of the specified type using the necessary data for building that shape and returns that shape
# e.g.: my_shape = ShapeFactory.create_shape("Circle", 2.0), where 2.0 is the radius of the circle
# e.g.: my_shape = ShapeFactory.create_shape("Rectangle", 2.0, 4.0), where 2.0 is length and 4.0 is width
# place the @staticmethod decorator/annotation on top of your create_shape definition to allow you to call it as shown in above examples
# NOTE: If you would like, you can instead have individual create methods for circle, square, triangle, and rectangle.
# This will get rid of the need for a big nested if else inside create_shape. Thus you could have create_circle, create_square, etc.
#

class ShapeFactory(Circle, Square, Rectangle, Triangle):

    def __init(self):
        # should ShapeFactory have an init? should the dict be in here? should it be "attached" to self by a period?
        # should this have what we put into it (ex: radius), or what comes out (ex: area, circumference?)
        self.shape_dict = {
        'Circle': [Circle, Circle.radius],
        'Square': [Square, Square.length, Square.width],
        'Rectangle': [Rectangle, Rectangle.length, Rectangle.width],
        'Triangle': [Triangle, Triangle.side1, Triangle.side2, Triangle.base, Triangle.height],
        }

    @staticmethod
    def create_shape(shape_name, shape_data):
        # shape data: shape_name, area, perimeter
        # rather than an if statement that searches for the right method to apply to the shape_data
        # create a dict to create the shape object. im open to other ways to write this.

        for shape_name in self.shape_dict:
            #but a static method doesn't have a "self" call. so should the dict be in this method instead?
            #first write a check that the number of arguments passed matches the length of the list for that dict_key
            #write code here to create the shape based on shape_name and shape_data

        #^^ if this doesnt work Varik said we can make indiv methods for each shape instead (would be simpler)

