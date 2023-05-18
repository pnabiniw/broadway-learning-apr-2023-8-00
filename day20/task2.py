try:
    a = int(input("Enter a number "))
    b = int(input("Enter another number "))
    print("Division result is ", a / b)
except ValueError:
    print("Enter a valid number")
except ZeroDivisionError:
    print("Please don't provide 0 in denominator")
