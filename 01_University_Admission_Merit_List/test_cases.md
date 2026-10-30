# Test Cases

Use these cases to check the admission conditions. Enter each applicant when the program prompts for their details.

| Test | Course | Maths | Physics | Chemistry | Expected result |
|---|---|---:|---:|---:|---|
| 1 | CSE | 85 | 82 | 83 | Eligible; aggregate 83.33 |
| 2 | CSE | 59 | 95 | 95 | Not eligible; Maths is below 60 |
| 3 | ECE | 70 | 72 | 68 | Eligible; aggregate 70.00 |
| 4 | MECH | 60 | 61 | 59 | Eligible; aggregate 60.00 |
| 5 | ECE | 49 | 90 | 90 | Not eligible; Maths is below 50 |
| 6 | CSE | 105 | 80 | 80 | Invalid marks |
| 7 | ART | 80 | 80 | 80 | Invalid course |

## Sample input scenario

For one CSE applicant:
- Number of applicants: 1
- Candidate name: Arun
- Course: CSE
- Mathematics: 85
- Physics: 82
- Chemistry: 83

## Expected key output

```text
Eligible for admission

UNIVERSITY ADMISSION MERIT LIST

Course: CSE
Rank: 1 | Name: Arun | Aggregate: 83.33 | Maths: 85.0 | Physics: 82.0
```

Run each case in VS Code and save screenshots of the actual terminal output. These expected results are for checking; they are not screenshots.
