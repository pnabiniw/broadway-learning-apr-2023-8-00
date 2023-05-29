# WAP to create a students CSV where the age of student is above 25

import csv

students = [
    {"id": "1", "name": "Arya", "age": 43},
    {"id": "2", "name": "Harry", "age": 23},
    {"id": "3", "name": "Jon", "age": 31},
    {"id": "4", "name": "Jane", "age": 20},
    {"id": "5", "name": "Krishna", "age": 26},
    {"id": "6", "name": "Eren", "age": 21},
    {"id": "7", "name": "John", "age": 30},
    {"id": "8", "name": "Nova", "age": 31},
    {"id": "9", "name": "Ram", "age": 17},
    {"id": "10", "name": "Jim", "age": 19},
]

with open("selected_students.csv", "w") as cw:  # cw is a file pointer
    field_names = students[0].keys()  # ["id", "name", "age"]
    csv_writer = csv.DictWriter(cw, fieldnames=field_names)
    csv_writer.writeheader()
    for student in students:
        if student["age"] > 25:
            csv_writer.writerow(student)
