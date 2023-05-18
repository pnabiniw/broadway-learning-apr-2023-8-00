class Circle:
    def __init__(self, radius):
        self.radius = radius

    def total_radius(self, obj):
        return self.radius + obj.radius

    def is_greater(self, obj):
        return self.radius > obj.radius

    def __gt__(self, obj):  # dunder method or the magic method __gt__
        return self.radius > obj.radius

    def __add__(self, other):  # __add__
        return self.radius + other.radius


c1 = Circle(10)
c2 = Circle(25)
print(c1.radius + c2.radius)

print(c1.total_radius(c2))

if c1.radius > c2.radius:
    print("c1 is greater")
else:
    print("c2 is greater")

print(c1.is_greater(c2))
print(c2.is_greater(c1))

print(c1.__gt__(c2))
print(c1 > c2)
print(c1 + c2)

