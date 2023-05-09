# Treating n as string
n = input("Enter a number ")
reverse = n[::-1]
print("Palindrome") if n == reverse else print("Not Palindrome")

# Treating n as integer
n = int(input("Enter a number "))  # 12347
b = n
reverse = 0
while n != 0:
    remainder = n % 10
    reverse = reverse * 10 + remainder  # 74321
    n = n // 10

print("Palindrome") if reverse == b else print("Not Palindrome")
