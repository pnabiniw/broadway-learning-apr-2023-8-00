# For loops in python

evens = [0, 2, 4, 5, 6, 8]  # Iteration in list
for value in evens:
    print(value)

nums = (1, 2, 3, 4)  # Iteration in tuple
for num in nums:
    print(num)

nums = {1, 2, 3, 4}  # Iteration in set
for num in nums:
    print(num)

message = "Hello World"  # Iteration in string
for m in message:
    print(m)



#### range() function ######

print(list(range(5)))   # Result => [0, 1, 2, 3, 4]

print(list(range(1, 10)))  # Result => [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(list(range(1, 10, 2)))  # Result => [1, 3, 5, 7, 9]

print(list(range(0, 10, 2)))  # Result => [0, 2, 4, 6, 8]

for i in range(5):
    print(i)

for i in range(2, 10, 2):
    print(i)


# If the value of loop variable is not needed inside the loop body, then we
# can use underscore

for _ in range(5):
    print("Hello World")
