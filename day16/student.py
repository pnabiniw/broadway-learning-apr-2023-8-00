class Student:
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department

    def get_info(self):  # This is a class method
        return f"Student name is {self.name}. Age is {self.age} and dept " \
               f"is {self.department}"


student1 = Student("Jon", 45, "CS")
print(student1.name)
print(student1.age)
print(student1.department)
print(student1.get_info())

student2 = Student("Jane", 23, "IT")
print(student2.name)
print(student2.age)
print(student2.department)
print(student2.get_info())
