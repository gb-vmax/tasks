# Bug Report

### Describe the bug

The calendar month view is displaying incorrect dates. When rendering a month, the days appear to be shifted or duplicated, causing the calendar to show the wrong dates for each week.

### Reproduction

```js
import { getMonthDays } from '@mantine/dates';

const monthDays = getMonthDays({
  month: new Date(2024, 0, 1), // January 2024
  firstDayOfWeek: 0, // Sunday
  consistentWeeks: true
});

// The returned weeks contain incorrect dates
// Days appear to be shifted by one day
console.log(monthDays);
```

### Expected behavior

The function should return the correct array of weeks with proper dates for the given month. Each week should contain 7 days in the correct order, and the dates should align properly with the calendar grid.

### System Info

- @mantine/dates version: latest
- Browser: Chrome

---
Repository: /testbed
