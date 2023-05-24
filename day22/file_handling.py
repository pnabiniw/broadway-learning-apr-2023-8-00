# Opening files in different modes:
# 1. r => Read Mode
# 2. w => Write Mode
# 3. a => Append Mode
# 4. x => Exclusive Write Mode
# 5. b => Binary Mode (rb, wb, r+b, w+b)
# 6. r+ => Read and Write Mode
# 7. w+ => Write and Read Mode
# 8. a+ => Append and Read Mode

filename = "info.txt"

# Write Mode
# fp = open(filename, "w")
# fp.write("Hello World")
# fp.close()
#
#
# Read Mode
# fp = open(filename, "r")
# data = fp.read()
# print(data)
# fp.close()


# Write and Read Mode
fp = open(filename, "w+")
fp.write("Python is a high level language")
fp.seek(0)  # Moves the file cursor to the very first location a file
data = fp.read()
print(data)
fp.close()


# Append Mode
fp = open(filename, "a")
fp.write("\nI'm learning Python")
fp.close()

# Exclusive write mode
# fp = open(filename, "x")
# fp.write("Hello World")
# fp.close()


# Context Manager
filename = "message.txt"
with open(filename, "w+") as fp:
    fp.write("Hello World")
    fp.seek(0)
    data = fp.read()
    print(data)

with open(filename, "a") as fp:
    fp.write("\nI am learning Python")


import test1  # Directly importing a module
from test1 import addition  # Importing function from a module

from day20.recursion import message
from day20 import recursion

