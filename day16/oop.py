# Creating a class A
class A:
    a = 1   # class attribute

    def __init__(self, b, c):   # __init__ is an constructor
        self.b = b   # Instance attribute
        self.c = c   # Instance attribute

    def get_a(self):  # This is a behavior also called as methods
        return self.a


obj1 = A(5, 4)  # creating an object of class A
print(obj1.a)
print(obj1.b)
print(obj1.c)

obj2 = A(10, 15)  # creating an object of class A
print(obj2.a)
print(obj2.b)
print(obj2.c)

abc = 1


# Characteristics of OOP
# 1. Inheritance  # Concept of parent and child classes
# 2. Encapsulation  # Concept of hiding methods and properties (Private, public, protected)
# 3. Polymorphism   # Different forms of same methods
# 4. Abstraction    # Making only required logic accessible to the end user
