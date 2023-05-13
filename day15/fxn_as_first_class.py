# Functions are objects
# Functions can be stored in data-structures
# Functions can be passed to another function
# Functions can be nested


# Functions can be stored in a variable
def addition(a, b):
    return a + b


print(addition(2, 3))

add = addition
print(add(4, 7))


# Functions can be stored in data-structures

data = [1, 2, add, lambda x, y: x + y, addition]
print(data)
