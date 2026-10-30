# Sum of Natural Numbers
n = int(input("Enter a non-negative integer: "))
if n < 0:
    print("Please enter a non-negative integer.")
else:
    counter = 1
    total = 0
    while counter <= n:
        total = total + counter
        counter = counter + 1
    print("Sum of first", n, "natural numbers:", total)
