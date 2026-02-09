# Bug Report

### Describe the bug

The `getEndOfWeek` function is returning incorrect dates. When I set a custom `firstDayOfWeek`, the function returns the wrong end-of-week date instead of calculating it properly based on the starting day.

### Reproduction

```js
import { getEndOfWeek } from '@mantine/dates';
import dayjs from 'dayjs';

// Example 1: firstDayOfWeek = 0 (Sunday)
const date1 = dayjs('2024-01-15'); // Monday
const endOfWeek1 = getEndOfWeek(date1, 0);
console.log(endOfWeek1.format('YYYY-MM-DD')); 
// Expected: 2024-01-20 (Saturday, end of week when week starts on Sunday)
// Actual: incorrect date

// Example 2: firstDayOfWeek = 1 (Monday)  
const date2 = dayjs('2024-01-15'); // Monday
const endOfWeek2 = getEndOfWeek(date2, 1);
console.log(endOfWeek2.format('YYYY-MM-DD'));
// Expected: 2024-01-21 (Sunday, end of week when week starts on Monday)
// Actual: incorrect date
```

### Expected behavior

The function should return the last day of the week based on the `firstDayOfWeek` parameter:
- If week starts on Sunday (0), it should end on Saturday (6)
- If week starts on Monday (1), it should end on Sunday (0)
- And so on for other starting days

### System Info
- @mantine/dates version: latest
- dayjs version: latest

---
Repository: /testbed
