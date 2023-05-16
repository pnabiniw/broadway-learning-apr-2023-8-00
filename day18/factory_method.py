from datetime import datetime


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, year):  # This is also called a factory method
        age = datetime.today().year - year
        return cls(name, age)


p1 = Person("Jon", 25)
print(p1.age)

p2 = Person.from_birth_year("Jane", 1990)
print(p2.age)


class Distance:
    def __init__(self, in_kms):
        self.in_kms = in_kms

    @classmethod
    def into_kms(cls, miles):   # This is a factory method
        return cls(miles * 1.6)

    @staticmethod
    def message(d):
        if d < 20:
            return "It is a short distance"
        return "It's way too long !!"


d1 = Distance(4)
print(d1.in_kms)

d2 = Distance.into_kms(4)   # Here input is 4 miles
print(d2.in_kms)

print(Distance.message(45))  # calling static method using class
print(d1.message(16))  # calling static method using an object

