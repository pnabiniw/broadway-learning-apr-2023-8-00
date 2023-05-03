# List Methods Continue

# pop() method takes index as a parameter and removes the element
# at the provided index
a = ["Hello", "from", "broadway", "I'm", "learning", "Python"]
value = a.pop(2)
# This pops out the element at 2nd index from the list i.e. broadway
# and returns the value to the variable
print(a)
print(value)

a.clear()   # This clears all the elements from the list and gives empty list []


a = [1, 2, 3, 4, 1, 5, 3, 2]
print(a.index(2))  # This gives the index of value 2 in the given list. In this
# case the index of 2 (at first occurence) is 1.

print(a.index(3, 3, 7))   # This gives 6 as 3 is searched in range 3rd to 6th position

print(a.count(3))  # this gives 2 because 3 is repeated two times in the list

a = ["Hello", "from", "Broadway"]
a.reverse()
print(a)  # result: ["Broadway", "from", "Hello"]


