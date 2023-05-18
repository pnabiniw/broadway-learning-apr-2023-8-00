# In python (or in any other language) there are three types of errors
# 1. Syntax Error
# 2. Logical Error
# 3. Exceptions / Runtime Error


try:
    num = int(input("Enter a number "))
except (ValueError, TypeError):
    print("Please enter a valid number ")
except IndexError:
    print("IndexError")
except ValueError:
    print("ValueError")
else:
    x = num
    y = num
    summ = x + y
    print(summ)
finally:
    print("Finally Executed")


# try:
#     fp = open("students.txt", "w")
#     print(fp)
#     a = 2
#     print(a)
# except:
#     print("Exception occurred")
# finally:
#     fp.close()
