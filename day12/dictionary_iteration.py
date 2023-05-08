####### Iteration in dictionary #######

student = {"name": "Jon", "age": 45, "department": "CS"}

for key in student:
    print(key)   # this gives keys of the dictionary 'name', 'age', 'department'


for value in student.values():
    print(value)  # this gives values of the dictionary "Jon", 45, "CS"

for key in student.keys():
    print(key)

for key, value in student.items():
    print(key)
    print(value)
