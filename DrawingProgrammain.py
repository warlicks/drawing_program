from draw.shape_factory import ShapeFactory
from draw.DrawingProgram import DrawingProgram

# Set up the shapes we want to create for the start of the program.
circles = [{"radius": 10}, {"radius": 100}]
squares = [{"length": 4}, {"length": 10}]
rectangles = [{"length": 10, "width": 20}]
triangle = [{"side1": 10, "side2": 20, "base": 10, "height": 30}]

# Use the shape factory to create the list of shapes to pass to DrawingProgram
all_shapes = []
for c in circles:
    all_shapes.append(ShapeFactory.create_shape("circle", **c))

for t in triangle:
    all_shapes.append(ShapeFactory.create_shape("triangle", **t))

for r in rectangles:
    all_shapes.append(ShapeFactory.create_shape("rectangle", **r))

for s in squares:
    all_shapes.append(ShapeFactory.create_shape("square", **s))


# Create the intial drawing program.
d = DrawingProgram(all_shapes)
d.add_shape(ShapeFactory.create_shape("rectangle", length=10, width=2))


print(d.get_shape(2))
