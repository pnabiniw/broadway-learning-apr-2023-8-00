"""
WAP to delete all the occurrences of a specified character in a given string
S = “All the occurrences of a specified character in a given string”
Input = “a”
Output = “ll occurrences of  specified chrcter in  given string”

"""

s = "All the occurrences of a specified character in a given string"
new_s = ""
char = input("Enter the character ")
for i in s:
    if i.lower() == char.lower():
        continue
    new_s += i
print(new_s)

