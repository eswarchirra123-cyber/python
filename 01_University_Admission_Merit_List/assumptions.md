# Assumptions

1. The number of applicants is entered as a non-negative integer.
2. Each applicant applies for one of these courses: CSE, ECE, or MECH.
3. Mathematics, Physics, and Chemistry marks are entered as numbers from 0 to 100.
4. Aggregate is the average of the three subject marks.
5. Course eligibility rules are:
   - CSE: aggregate at least 80 and every subject mark at least 60.
   - ECE: aggregate at least 70 and every subject mark at least 50.
   - MECH: aggregate at least 60 and every subject mark at least 40.
6. Invalid marks and unsupported course names are rejected.
7. Merit order is course name ascending, aggregate descending, Mathematics descending, Physics descending, and candidate name ascending.
8. The program does not use a database; applicant information is held in memory while the program runs.
