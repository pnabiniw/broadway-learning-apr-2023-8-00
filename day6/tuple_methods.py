# Tuple has two methods index() and count()

t = (0, 1, 2, 3, 4)
print(t.index(4))  # This gives 4
print(t.count(3))  # This gives 1

t = (1, 1, 2, 2, 2, 2)
print(t.count(2))  # This gives 4


# Built-in functions

t = (1, 2, 3, 4)
result = sum(t)
print(result)  # This gives 10

result = max(t)
print(result)  # result => 4

result = min(t)
print(result)  # result => 1


t = (5, 2, 4, 1, 10, 12, 9)
print(sorted(t))
# this gives [1, 2, 4, 5, 9, 10, 12]
print(sorted(reverse=True))
# this gives [12, 10, 9, 5, 4, 2, 1]

result = reversed(t)
print(list(result))  # This reversed the sequence. This is not
# descend order sort. Result => [9, 12, 10, 1, 4, 2, 5]


