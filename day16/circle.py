# Create a class Circle. The circle object should have radius as property and
# area() as a method

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return f"Area is {(22/7) * self.radius ** 2}"

    def change_radius(self, radius):  # Method to set the value
        self.radius = radius


circle1 = Circle(3)
print(circle1.area())  # Get attribute of the object
circle1.change_radius(4)
print(circle1.area())

circle2 = Circle(5)
print(circle2.area())
circle2.change_radius(8)
print(circle2.area())

circle1.radius = 50  # Setting  value to obj (circle1)
print(circle1.area())

circle2.radius = 20  # Setting  value to obj (circle1)
print(circle2.area())
