# Program 02: Student Grade Calculator

mark1 = float(input("Enter marks in subject 1: "))
mark2 = float(input("Enter marks in subject 2: "))
mark3 = float(input("Enter marks in subject 3: "))

if (mark1 < 0 or mark1 > 100 or
        mark2 < 0 or mark2 > 100 or
        mark3 < 0 or mark3 > 100):
    print("Invalid marks. Enter marks between 0 and 100.")

else:
    total = mark1 + mark2 + mark3
    average = total / 3

    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    else:
        grade = "F"

    print("Total marks:", total)
    print("Average marks:", round(average, 2))
    print("Grade:", grade)
