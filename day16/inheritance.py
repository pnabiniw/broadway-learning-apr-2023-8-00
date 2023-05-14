# Single Inheritance

class A:  # Parent class
    a = 3


class B(A):  # B is a derived / child class
    c = 4


obj = B()
print(obj.c)
print(obj.a)


class Vehicle:
    def __init__(self, color, doors):
        self.color = color
        self.doors = doors

    def get_vehicle_info(self):
        return f"Vehicle color is {self.color} and it has {self.doors} doors"


class Car(Vehicle):
    def __init__(self, mileage, color, doors):
        self.mileage = mileage
        super().__init__(color, doors)

    def get_vehicle_info(self):
        print(super().get_vehicle_info())
        return f"vehicle mileage is {self.mileage}"


rover = Car(50, 'red', 4)
print(rover.get_vehicle_info())
