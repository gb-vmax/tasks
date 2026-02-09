# Bug Report

### Describe the bug

The `getEndOfWeek` function is returning incorrect dates. When I pass a date and specify the first day of week, the returned end-of-week date doesn't match what I'd expect.

### Reproduction

```js
import { getEndOfWeek } from '@mantine/dates';

// Example: If Monday (1) is the first day of the week
// Then Sunday (0) should be the last day of the week
const date = new Date('2024-01-15'); // This is a Monday
const endOfWeek = getEndOfWeek(date, 1);

// Expected: Should return the following Sunday (2024-01-21)
// Actual: Returns Monday (2024-01-15) - the same date!
console.log(endOfWeek);

// Another example with Sunday as first day
const endOfWeek2 = getEndOfWeek(date, 0);
// Expected: Should return Saturday (2024-01-20)
// Actual: Returns Sunday (2024-01-14) - wrong week!
```

### Expected behavior

`getEndOfWeek` should calculate the last day of the current week based on the `firstDayOfWeek` parameter. For example:
- If `firstDayOfWeek` is 1 (Monday), the end should be Sunday
- If `firstDayOfWeek` is 0 (Sunday), the end should be Saturday

Currently it's returning dates that don't make sense for the end of the week.

### System Info
- @mantine/dates version: latest
- Browser: Chrome

---
Repository: /testbed
