"""
CSV = Comma Separated Values
Way of storing the data in comma separated forms

id,name,age
1,Harry,23     => This is an example of a CSV

"""
import csv
from day25.estd_connection import estd_connection


def insert(student_id, name, age):
    cursor = estd_connection()
    sql = f"""
        INSERT INTO STUDENT (ID, NAME, AGE) VALUES 
        ('{student_id}', '{name}', {age})
    """
    cursor.execute(sql)
    print("Student added successfully!!")


with open("students.csv", "r") as cr:
    csv_reader = csv.reader(cr)  # This returns an iterator
    next(csv_reader)
    for each_line in csv_reader:
        id = each_line[0]
        name = each_line[1]
        age = each_line[2]
        insert(id, name, age)

    # Using comprehension
    # students = [each_line[1] for each_line in students]

