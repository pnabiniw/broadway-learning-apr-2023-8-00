class Department:
    def __init__(self, name, no_of_student):
        self.name = name
        self.no_of_student = no_of_student

    def total_students(self, *args):
        students_list = []
        for obj in args:
            students_list.append(obj.no_of_student)
        students = sum(students_list)
        return self.no_of_student + students


d1 = Department("CS", 20)
d2 = Department("Math", 10)
d3 = Department("Civil", 30)
d4 = Department("Civil", 5)

print(d1.total_students(d2, d3, d4))
