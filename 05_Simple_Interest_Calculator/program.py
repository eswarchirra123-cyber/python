# Simple Interest Calculator
principal = float(input("Enter principal amount: "))
rate = float(input("Enter annual rate of interest: "))
time = float(input("Enter time in years: "))
if principal < 0 or rate < 0 or time < 0:
    print("Please enter non-negative values.")
else:
    interest = (principal * rate * time) / 100
    total_amount = principal + interest
    print("Simple interest: Rs.", round(interest, 2))
    print("Total amount: Rs.", round(total_amount, 2))
