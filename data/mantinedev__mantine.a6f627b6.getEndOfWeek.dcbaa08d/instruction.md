# Bug Report

### Describe the bug

The `getEndOfWeek` function is returning incorrect dates when calculating the end of the week. The function seems to be stuck in an infinite loop or returns the wrong day depending on the `firstDayOfWeek` parameter.

### Reproduction

```js
import { getEndOfWeek } from '@mantine/dates';

// Example 1: firstDayOfWeek = 0 (Sunday)
const date1 = new Date('2024-01-15'); // Monday
const endOfWeek1 = getEndOfWeek(date1, 0);
// Expected: Saturday (2024-01-20)
// Actual: Function hangs or returns wrong date

// Example 2: firstDayOfWeek = 1 (Monday)  
const date2 = new Date('2024-01-15'); // Monday
const endOfWeek2 = getEndOfWeek(date2, 1);
// Expected: Sunday (2024-01-21)
// Actual: Function hangs or returns wrong date
```

### Expected behavior

When `firstDayOfWeek` is 0 (Sunday), the function should return the Saturday of that week.
When `firstDayOfWeek` is 1 (Monday), the function should return the Sunday of that week.

The function should consistently calculate the last day of the week based on the provided `firstDayOfWeek` parameter.

### System Info
- @mantine/dates version: latest
- Browser: Chrome 120

---
Repository: /testbed
