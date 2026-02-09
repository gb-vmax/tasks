# Bug Report

### Describe the bug

The `getMonthDays` function is generating incorrect month calendars. The first day of the month is being skipped, and there's an extra week being added to the calendar grid.

### Reproduction

```js
import { getMonthDays } from '@mantine/dates';

// Try to get days for January 2024
const days = getMonthDays({
  month: new Date(2024, 0, 1), // January 1, 2024
  firstDayOfWeek: 1
});

// The first day (January 1st) is missing from the calendar
// Also getting 7 weeks instead of the expected 6 weeks maximum
console.log(days.length); // Shows 7 weeks
console.log(days[0]); // First week doesn't start with January 1st
```

### Expected behavior

The calendar should:
1. Include all days of the month starting from the 1st
2. Generate a maximum of 6 weeks when `consistentWeeks` is enabled
3. Properly align the first day of the month with the correct day of the week

### System Info
- @mantine/dates version: latest
- Browser: Chrome

---
Repository: /testbed
