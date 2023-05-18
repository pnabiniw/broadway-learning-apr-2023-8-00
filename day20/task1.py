try:
    a = int(input("Enter a number "))
    b = int(input("Enter another number "))
except ValueError:
    print("Please enter a valid number")
else:
    print("Sum of the provided numbers is", a + b)
