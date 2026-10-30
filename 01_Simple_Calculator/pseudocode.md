# Pseudocode

```text
START
    INPUT first_number
    INPUT second_number
    INPUT operator

    IF operator is "+" THEN
        result = first_number + second_number
        DISPLAY result
    ELSE IF operator is "-" THEN
        result = first_number - second_number
        DISPLAY result
    ELSE IF operator is "*" THEN
        result = first_number * second_number
        DISPLAY result
    ELSE IF operator is "/" THEN
        IF second_number is 0 THEN
            DISPLAY "Cannot divide by zero"
        ELSE
            result = first_number / second_number
            DISPLAY result
        END IF
    ELSE
        DISPLAY "Invalid operator"
    END IF
STOP
```
