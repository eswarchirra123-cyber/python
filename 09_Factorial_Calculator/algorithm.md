# Algorithm

1. Start.
2. Read n.
3. If n is negative, display invalid input.
4. Otherwise set factorial = 1.
5. Repeat i from 1 through n and multiply factorial by i.
6. Display factorial and stop.

## Flowchart

```mermaid
flowchart TD
 A([Start]) --> B[/Input n/]
 B --> C{n < 0?}
 C -->|Yes| D[Display invalid input]
 C -->|No| E[Set factorial = 1 and i = 1]
 E --> F{i <= n?}
 F -->|Yes| G[factorial = factorial * i]
 G --> H[Increase i by 1]
 H --> F
 F -->|No| I[/Display factorial/]
 D --> J([Stop])
 I --> J
```
