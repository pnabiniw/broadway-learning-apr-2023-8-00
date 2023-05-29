# WAP to read the students csv and create a new csv file where student age is
# greater than 25

import csv

with open("students.csv", "r") as cr:
    csv_reader = csv.DictReader(cr)

    with open("new_students.csv",  "w") as cw:
        field_names = ["id", "name", "age"]
        csv_writer = csv.DictWriter(cw, fieldnames=field_names)
        csv_writer.writeheader()
        for each_line in csv_reader:
            if each_line['age'] > "25":
                csv_writer.writerow(each_line)
