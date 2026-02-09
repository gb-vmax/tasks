# Bug Report

### Describe the bug

The `getStartOfWeek` function is returning incorrect dates. Instead of going backwards to find the start of the week, it appears to be moving forward in time, which results in dates that are in the future relative to the input date.

### Reproduction

```js
import { getStartOfWeek } from '@mantine/dates';

// Example: Get start of week for a Wednesday
const date = '2024-01-10'; // Wednesday, Jan 10, 2024
const startOfWeek = getStartOfWeek(date, 1); // firstDayOfWeek = Monday

console.log(startOfWeek); 
// Expected: '2024-01-08' (Monday, Jan 8)
// Actual: Returns a date in the future instead of the past
```

### Expected behavior

When calling `getStartOfWeek`, it should return the date of the first day of the week (e.g., Monday) that comes **before or on** the given date. For example, if the input is Wednesday Jan 10, 2024 and `firstDayOfWeek` is set to Monday (1), it should return Monday Jan 8, 2024.

Currently, the function seems to be calculating the start of week incorrectly by going forward instead of backward.

### System Info
- @mantine/dates version: latest
- dayjs version: latest

---
Repository: /testbed
