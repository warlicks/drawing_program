from shapes import Circle, Square, Rectangle, Triangle

#         create_shape(shape name, shape data): creates a shape of the specified type using the necessary data for building that shape and returns that shape
#             e.g.: my_shape = ShapeFactory.create_shape("Circle", 2.0), where 2.0 is the radius of the circle
#             e.g.: my_shape = ShapeFactory.create_shape("Rectangle", 2.0, 4.0), where 2.0 is length and 4.0 is width
#             place the @staticmethod decorator/annotation on top of your create_shape definition to allow you to call it as shown in above examples
#             NOTE: If you would like, you can instead have individual create methods for circle, square, triangle, and rectangle.
#     This will get rid of the need for a big nested if else inside create_shape. Thus you could have create_circle, create_square, etc.
#

class ShapeFactory(Circle, Square, Rectangle, Triangle):

    def __init(self):
        self