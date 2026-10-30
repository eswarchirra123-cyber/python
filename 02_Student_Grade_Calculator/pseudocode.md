# Pseudocode

```text
START
    INPUT mark1, mark2, mark3

    IF any mark is less than 0 OR greater than 100 THEN
        DISPLAY "Invalid marks"
    ELSE
        total = mark1 + mark2 + mark3
        average = total / 3

        IF average >= 90 THEN
            grade = "A"
        ELSE IF average >= 80 THEN
            grade = "B"
        ELSE IF average >= 70 THEN
            grade = "C"
        ELSE IF average >= 60 THEN
            grade = "D"
        ELSE
            grade = "F"
        END IF

        DISPLAY total, average, grade
    END IF
STOP
```
