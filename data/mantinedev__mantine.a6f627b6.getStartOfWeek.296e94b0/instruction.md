# Bug Report

### Describe the bug

The `getStartOfWeek` function is returning incorrect dates when calculating the start of the week. Instead of going backwards to find the start of the week, it appears to be jumping forward by 6 days, which produces completely wrong results.

### Reproduction

```js
import { getStartOfWeek } from '@mantine/dates';

// Example: Get start of week for a date in the middle of the week
const date = '2024-01-17'; // Wednesday
const startOfWeek = getStartOfWeek(date, 1); // firstDayOfWeek = Monday

console.log(startOfWeek);
// Expected: '2024-01-15' (Monday of that week)
// Actual: Returns a date far in the future instead of going back to Monday
```

### Expected behavior

The function should return the date of the first day of the week by going backwards from the given date. For example, if you pass a Wednesday and set `firstDayOfWeek` to Monday (1), it should return the Monday of that same week.

### System Info

- @mantine/dates version: latest
- dayjs version: latest

This seems to have started happening recently. The logic for finding the start of the week seems to be going in the wrong direction.

---
Repository: /testbed
