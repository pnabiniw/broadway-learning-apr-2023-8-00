## Lambda / Anonymous function
# Lambda functions are the one liner functions in Python.
# They don't have name. So, they are called as anonymous
# functions

def addition(a, b):
    return a + b  # This is a normal function


# This is a lambda function
add = lambda a, b: a + b
print(add(3, 4))

a = [(3, 6), (1, 2), (4, 5), (2, 1)]

a.sort(key=lambda data: data[1])
print(a)

# Higher Order Functions
# If a function takes another function as a parameter then
# it is a higher order function
# map(), filter() and reduce() are the examples of higher
# order function

# map() function

a = [1, 2, 3, 4, 5]

# def multiple_of_two(data):
#     return data * 2

result = map(lambda data: data * 2, a)
print(list(result))   # Result [2, 4, 6, 8, 10]

# filter() function
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# def get_even_nums(data):
#     return data % 2 == 0

result = filter(lambda data: data % 2 == 0, a)
print(list(result))

# import os
# def clear():
#     os.system('cls')
#
# clear()

students = [{"name": "Jon", "age": 19},
            {"name": "Jane", "age": 45},
            {"name": "Harry", "age": 15},
            {"name": "Arya", "age": 34},
            ]
# [{"name": "Jon", "age": 19}, {"name": "Harry", "age": 15}]

result = filter(lambda data: data['age'] < 20, students)
print(list(result))


a = [1, 2, 3, 4]
result = filter(lambda x: x ** 2, a)
print(list(result))    # [1, 2, 3, 4]


a = [1, 5, 3, 15, 9, 10]
result = map(lambda x: x % 5 == 0, a)
print(list(result))   # [False, True, False, True, False, True]


# reduce() function
from functools import reduce

a = [1, 2, 3, 4, 5]   # (((1+2) + 3) + 4) + 5 = 15
result = reduce(lambda x, y: x + y, a)
print(result)   # Result = 15
