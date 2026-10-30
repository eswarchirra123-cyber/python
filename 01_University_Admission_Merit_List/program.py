# Case Study 01: University Admission Merit List

n = int(input("Number of applicants: "))
eligible = []

for i in range(n):
    print("\nApplicant", i + 1)
    name = input("Candidate name: ")
    course = input("Course (CSE/ECE/MECH): ").upper()

    maths = float(input("Mathematics marks: "))
    physics = float(input("Physics marks: "))
    chemistry = float(input("Chemistry marks: "))

    valid = (0 <= maths <= 100 and
             0 <= physics <= 100 and
             0 <= chemistry <= 100)

    if not valid:
        print("Invalid marks")
        continue

    aggregate = (maths + physics + chemistry) / 3

    if course == "CSE":
        cutoff = 80
        minimum = 60
    elif course == "ECE":
        cutoff = 70
        minimum = 50
    elif course == "MECH":
        cutoff = 60
        minimum = 40
    else:
        print("Invalid course")
        continue

    if (aggregate >= cutoff and
        maths >= minimum and
        physics >= minimum and
        chemistry >= minimum):

        eligible.append((name, course, aggregate,
                         maths, physics))
        print("Eligible for admission")
    else:
        print("Not eligible")

# Rank using selection sort
for i in range(len(eligible)):
    best = i

    for j in range(i + 1, len(eligible)):
        a = eligible[j]
        b = eligible[best]

        if (a[1] < b[1] or
            (a[1] == b[1] and a[2] > b[2]) or
            (a[1] == b[1] and a[2] == b[2]
             and a[3] > b[3]) or
            (a[1] == b[1] and a[2] == b[2]
             and a[3] == b[3] and a[4] > b[4]) or
            (a[1] == b[1] and a[2] == b[2]
             and a[3] == b[3] and a[4] == b[4]
             and a[0] < b[0])):
            best = j

    eligible[i], eligible[best] = eligible[best], eligible[i]

print("\nUNIVERSITY ADMISSION MERIT LIST")

previous_course = ""
rank = 0

for candidate in eligible:
    name, course, aggregate, maths, physics = candidate

    if course != previous_course:
        previous_course = course
        rank = 0
        print("\nCourse:", course)

    rank += 1

    print("Rank:", rank,
          "| Name:", name,
          "| Aggregate:", round(aggregate, 2),
          "| Maths:", maths,
          "| Physics:", physics)

if len(eligible) == 0:
    print("No eligible candidates")
