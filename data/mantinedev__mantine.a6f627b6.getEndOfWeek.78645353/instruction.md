# Bug Report

### Describe the bug

The `getEndOfWeek` function is returning incorrect dates when calculating the end of a week. It seems to be adding days infinitely or returning the wrong end-of-week date depending on the `firstDayOfWeek` setting.

### Reproduction

```js
import { getEndOfWeek } from '@mantine/dates';
import dayjs from 'dayjs';

// Example 1: Week starting on Sunday (firstDayOfWeek = 0)
const date1 = dayjs('2024-01-15'); // Monday
const endOfWeek1 = getEndOfWeek(date1, 0);
console.log(endOfWeek1.format('YYYY-MM-DD')); 
// Expected: 2024-01-20 (Saturday, since week starts Sunday)
// Getting: incorrect date or infinite loop

// Example 2: Week starting on Monday (firstDayOfWeek = 1)
const date2 = dayjs('2024-01-15'); // Monday
const endOfWeek2 = getEndOfWeek(date2, 1);
console.log(endOfWeek2.format('YYYY-MM-DD'));
// Expected: 2024-01-21 (Sunday, since week starts Monday)
// Getting: incorrect date or infinite loop
```

### Expected behavior

The function should correctly calculate the last day of the week based on the `firstDayOfWeek` parameter. If the week starts on Sunday (0), the end should be Saturday (6). If the week starts on Monday (1), the end should be Sunday (0).

### System Info

- @mantine/dates version: latest
- dayjs version: latest

---
Repository: /testbed
