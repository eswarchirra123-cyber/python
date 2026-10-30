# Algorithm

1. Start.
2. Read units consumed.
3. If units are negative, display invalid input.
4. If units <= 100, bill = units * 1.50.
5. Else if units <= 200, bill = 150 + (units - 100) * 2.50.
6. Otherwise, bill = 400 + (units - 200) * 4.00.
7. Display bill and stop.

## Flowchart

```mermaid
flowchart TD
 A([Start]) --> B[/Input units/]
 B --> C{Units < 0?}
 C -->|Yes| D[Invalid units]
 C -->|No| E{Units <= 100?}
 E -->|Yes| F[Bill = units * 1.50]
 E -->|No| G{Units <= 200?}
 G -->|Yes| H[Bill = 150 + excess * 2.50]
 G -->|No| I[Bill = 400 + excess * 4.00]
 F --> J[/Display bill/]
 H --> J
 I --> J
 D --> K([Stop])
 J --> K
```
