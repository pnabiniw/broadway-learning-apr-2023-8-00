def factorial(num):
    # Factorial code
    result = 1
    for i in range(1, num+1):   # 1, 2, 3, 4, 5
        result = result * i
    return result


print(factorial(5))


# 5 factorial using reduce function
from functools import reduce
result = reduce(lambda x, y: x * y, range(1, 6))
print(result)


# Factorial using recursion
def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num-1)

# 5 * factorial(4)  5 * 24 = 120
# 4 * factorial(3)  4* 6 = 24
# 3 * factorial(2)  3 * 2 = 6
# 2 * factorial(1)  2 * 1 = 2
# 1 * factorial(0)  1 * 1 = 1


print(factorial(5))

