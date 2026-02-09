# Bug Report

### Describe the bug

The calendar month view is showing incorrect dates when `hideWeekdays` is enabled. The dates appear to be off by one day, and the last week of the month is sometimes missing or contains wrong dates.

### Reproduction

```js
import { getMonthDays } from '@mantine/dates';

const result = getMonthDays({
  month: new Date(2024, 0, 1), // January 2024
  firstDayOfWeek: 0, // Sunday
  consistentWeeks: true,
  hideWeekdays: false
});

// The dates in the result are shifted by one day
// The last week may be incomplete or missing
console.log(result);
```

### Expected behavior

The month should display the correct dates for each day, with all weeks properly filled when `consistentWeeks` is enabled. Each day should correspond to the actual calendar date, not be shifted by one day.

### System Info

- @mantine/dates version: latest
- Browser: Chrome

---
Repository: /testbed
