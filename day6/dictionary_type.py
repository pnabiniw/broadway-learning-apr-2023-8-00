# Dictionary type is the key-value pair data type
# Empty dictionary can be created using curly braces {} or dict() built-in function

student = dict()  # This is an empty dictionary
print(student)
student = {}  # This is also an empty dictionary
print(student)

student = {"name": "Jon", "age": 45, "department": "CS"}  # Non-empty dictionary
print(student)
student = dict(name="Jon", age=45, department="CS")  # Non-empty dictionary
print(student)

student = dict([
    ("name", "Jon"),
    ("age", 43),
    ("department", "CS"),
])
print(student)  # This is also a dictionary


# Accesing values in dictionary

student = {"name": "Jon", "age": 45, "department": "CS"}
name = student['name']
print(name)  # Result => Jon

print(student['department'])  # Result => CS
# print(student["roll_number"])  # This raises KeyError because 'roll_number' is not
# a key of dictionary student

# We can also access the dictionary values using get() method
name = student.get('name')
print(name)

roll_number = student.get('roll_number')
print(roll_number)  # This gives None. If the key not present in the dictionary is
# provided to the get() method then it returns None


# We can also provide a default value to the get() method
roll = student.get("roll_number", 4)  # Here 4 is a default value
print(roll)  # This gives 4

name = student.get("name", "Jane")  # Here Jane is a default value
print(name)  # Result => Jon


# Adding and updating dictionary
student = {"name": "Jon", "age": 45, "department": "CS"}
student["roll"] = 4
print(student)  # Result => {"name": "Jon", "age": 45, "department": "CS", "roll": 4}

# If the key is already present in the dictionary then it gets updated
student['name'] = "Jane"
# Result => {"name": "Jane", "age": 45, "department": "CS", "roll": 4}

# Updating dictionary using update() method
student = {"name": "Jon", "age": 45}
student.update({"department": "CS", "roll": 4})
print(student)
# Result => {"name": "Jon", "age": 45, "department": "CS", "roll": 4}

student.update(id=1, height=5.8)
print(student)
# Result => {"name": "Jon", "age": 45, "department": "CS", "roll": 4, "id": 1,
# "height": 5.8}



# Deleting / Removing dictionary key-values
student = {
    "name": "Jon",
    "age": 45,
    "department": "CS",
    "roll": 4,
    "id": 1,
    "height": 5.8
}
roll = student.pop("roll")
print(student)  # roll key is removed from the dictionary
print(roll)  # 4]



# Rules for Dictionary Keys and Values
# 1. Dictionary keys must be immutable
# 2. Dictionary values can be of any data-type
# 3. A tuple can also be a dictionary key because it is immutable type. But,
#    if it contains mutable type, then it can't be used as a key

#    E.g d = {(1, 2, [1, 2]): "Hello"}   # This is invalid



# Membership Operation in Dictionary

student = {"name": "Jon", "age": 23}
print("age" in student)  # True. Membership is checked in keys in a dictionary
print("department" in student)  # False




