# Bug Report

### Describe the bug

The `getStartOfWeek` function is returning incorrect dates when calculating the start of the week. The returned date doesn't match the expected first day of the week based on the `firstDayOfWeek` parameter.

### Reproduction

```js
import { getStartOfWeek } from '@mantine/dates';

// Example 1: Get start of week for a Wednesday with Monday as first day
const result1 = getStartOfWeek('2024-01-10', 1); // Jan 10, 2024 is a Wednesday
console.log(result1); // Expected: 2024-01-08 (Monday), but getting wrong date

// Example 2: Get start of week for a Sunday with Monday as first day  
const result2 = getStartOfWeek('2024-01-14', 1); // Jan 14, 2024 is a Sunday
console.log(result2); // Expected: 2024-01-08 (Monday), but getting wrong date

// Example 3: Different first day of week
const result3 = getStartOfWeek('2024-01-10', 0); // 0 = Sunday as first day
console.log(result3); // Expected: 2024-01-07 (Sunday), but getting wrong date
```

### Expected behavior

The function should return the date of the first day of the week containing the given date, based on the `firstDayOfWeek` parameter. For example, if `firstDayOfWeek` is 1 (Monday) and the input date is a Wednesday, it should return the Monday of that week.

### System Info

- @mantine/dates version: latest
- dayjs version: latest

---
Repository: /testbed
