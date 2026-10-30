# Pseudocode

```text
START
 INPUT units
 IF units < 0 THEN DISPLAY invalid units
 ELSE IF units <= 100 THEN bill = units * 1.50
 ELSE IF units <= 200 THEN bill = 150 + (units - 100) * 2.50
 ELSE bill = 400 + (units - 200) * 4.00
 DISPLAY bill when units are valid
STOP
```
