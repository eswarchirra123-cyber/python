# Python Operator Explorer
a=float(input("First number: "))
b=float(input("Second number: "))
print("Addition:",a+b,"Subtraction:",a-b,"Multiplication:",a*b)
if b != 0: print("Division:",a/b)
else: print("Division by zero is not allowed")
print("a greater than b:",a>b,"Equal:",a==b)
print("Both positive:",a>0 and b>0)
count=5
count+=2
print("Assignment result:",count)
word="python"
print("'py' in word:", "py" in word)
other=word
print("other is word:",other is word)
