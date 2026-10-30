# Python Operator Explorer
# Syllabus topics: input/output, type conversion, arithmetic, relational, logical, assignment, membership, identity, expressions and precedence
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
if b != 0:
    print("Division:", a / b)
else:
    print("Division: not possible (division by zero)")
print("First is greater:", a > b)
print("Both are equal:", a == b)
print("Both positive:", a > 0 and b > 0)
count = 5
count += 2
print("Assignment operator result:", count)
word = "python"
print("'py' in word:", "py" in word)
first = word
print("first is word:", first is word)
