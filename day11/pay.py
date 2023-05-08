hour = float(input("Enter hours "))
rate = float(input("Enter hourly rate "))

if hour <= 40:
    pay = hour * rate

else:
    ot = hour - 40
    normal_pay = 40 * rate
    ot_pay = ot * rate * 1.5
    pay = normal_pay + ot_pay

print("Received payment ", pay)
