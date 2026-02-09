# Bug Report

### Describe the bug

The calendar is displaying an incorrect date range for the month. It looks like the first day of the month is being skipped, and the calendar is starting from the day before the actual month begins.

### Reproduction

```js
import { getMonthDays } from '@mantine/dates';

// Try to get days for January 2024
const days = getMonthDays({
  month: new Date(2024, 0, 15), // January 2024
  firstDayOfWeek: 1
});

// The first day shown should be January 1st, but it's showing December 31st instead
console.log(days[0][0]); // Expected: 2024-01-01, Actual: 2023-12-31
```

When rendering a month view, the calendar appears to be off by one day. The month starts one day earlier than it should, which causes the entire calendar grid to be shifted.

### Expected behavior

The `getMonthDays` function should return the correct date range for the specified month. The first day of the month should be included in the output, not the day before it.

### System Info
- @mantine/dates version: latest
- dayjs version: latest

---
Repository: /testbed
