# Algorithm

1. Start.
2. Read principal, rate and time.
3. Check that all values are non-negative.
4. Calculate SI = P * R * T / 100.
5. Calculate total amount = P + SI.
6. Display SI and total amount.
7. Stop.

## Flowchart

```mermaid
flowchart TD
 A([Start]) --> B[/Input P, R, T/]
 B --> C{Any value negative?}
 C -->|Yes| D[Invalid values]
 C -->|No| E[SI = P * R * T / 100]
 E --> F[Amount = P + SI]
 F --> G[/Display SI and amount/]
 D --> H([Stop])
 G --> H
```
