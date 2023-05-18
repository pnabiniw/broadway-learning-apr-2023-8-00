student = {"id": 1, "name": "Jane", "age": 45, "department": "Mathematics"}
key = input("Enter the info you want to get ")
try:
    result = student[key]
except KeyError:
    print("Invalid Key")
else:
    print(f"The {key} of the student is {result}")
