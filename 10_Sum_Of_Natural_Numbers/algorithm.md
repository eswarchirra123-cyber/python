# Algorithm

1. Start.
2. Read n.
3. If n is negative, display invalid input.
4. Set counter = 1 and total = 0.
5. While counter <= n, add counter to total and increase counter by 1.
6. Display total and stop.

## Flowchart

```mermaid
flowchart TD
 A([Start]) --> B[/Input n/]
 B --> C{n < 0?}
 C -->|Yes| D[Display invalid input]
 C -->|No| E[Set counter = 1 and total = 0]
 E --> F{counter <= n?}
 F -->|Yes| G[Add counter to total]
 G --> H[Increase counter by 1]
 H --> F
 F -->|No| I[/Display total/]
 D --> J([Stop])
 I --> J
```
