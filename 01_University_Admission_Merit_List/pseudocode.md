# Pseudocode

```text
START
    INPUT number_of_applicants
    eligible = empty list

    FOR each applicant
        INPUT name, course
        INPUT maths, physics, chemistry

        IF any mark is outside 0 to 100
            DISPLAY "Invalid marks"
            CONTINUE to next applicant
        END IF

        aggregate = (maths + physics + chemistry) / 3

        IF course is CSE
            cutoff = 80
            minimum = 60
        ELSE IF course is ECE
            cutoff = 70
            minimum = 50
        ELSE IF course is MECH
            cutoff = 60
            minimum = 40
        ELSE
            DISPLAY "Invalid course"
            CONTINUE to next applicant
        END IF

        IF aggregate >= cutoff AND every subject mark >= minimum
            ADD applicant details to eligible
            DISPLAY "Eligible for admission"
        ELSE
            DISPLAY "Not eligible"
        END IF
    END FOR

    SORT eligible using selection sort and merit rules
    DISPLAY course-wise ranks

    IF eligible is empty
        DISPLAY "No eligible candidates"
    END IF
STOP
```
