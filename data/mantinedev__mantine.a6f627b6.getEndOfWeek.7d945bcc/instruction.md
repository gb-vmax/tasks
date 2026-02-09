# Bug Report

### Describe the bug

The `getEndOfWeek` function is returning incorrect dates when calculating the end of the week. It seems to be returning the wrong day based on the `firstDayOfWeek` parameter.

### Reproduction

```js
import { getEndOfWeek } from '@mantine/dates';

// When firstDayOfWeek is 0 (Sunday)
const date1 = new Date('2024-01-15'); // Monday
const endOfWeek1 = getEndOfWeek(date1, 0);
// Expected: Saturday (2024-01-20)
// Actual: Returns wrong date

// When firstDayOfWeek is 1 (Monday)
const date2 = new Date('2024-01-15'); // Monday
const endOfWeek2 = getEndOfWeek(date2, 1);
// Expected: Sunday (2024-01-21)
// Actual: Returns wrong date
```

### Expected behavior

The function should return the last day of the week based on the `firstDayOfWeek` parameter:
- If week starts on Sunday (0), it should end on Saturday (6)
- If week starts on Monday (1), it should end on Sunday (0)
- And so on for other starting days

### System Info

- @mantine/dates version: latest
- Browser: Chrome 120

---
Repository: /testbed
