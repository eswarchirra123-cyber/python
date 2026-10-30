# Electricity Bill Calculator
units = float(input("Enter electricity units consumed: "))
if units < 0:
    print("Invalid units.")
elif units <= 100:
    bill = units * 1.50
    print("Electricity bill: Rs.", round(bill, 2))
elif units <= 200:
    bill = 100 * 1.50 + (units - 100) * 2.50
    print("Electricity bill: Rs.", round(bill, 2))
else:
    bill = 100 * 1.50 + 100 * 2.50 + (units - 200) * 4.00
    print("Electricity bill: Rs.", round(bill, 2))
