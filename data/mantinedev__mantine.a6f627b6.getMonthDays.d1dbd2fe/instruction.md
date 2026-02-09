# Bug Report

### Describe the bug

The calendar is displaying incorrect dates for the month view. The first day of the month seems to be shifted by one day, and the last week of the month is missing from the display.

### Reproduction

```js
import { getMonthDays } from '@mantine/dates';

const monthDays = getMonthDays({
  month: new Date(2024, 0, 1), // January 2024
  firstDayOfWeek: 0, // Sunday
  consistentWeeks: false
});

// The first day shown is December 31, 2023 instead of December 30, 2023
// The last week of January is not included in the output
console.log(monthDays);
```

### Expected behavior

The calendar should display complete weeks, starting from the correct day before the first of the month and including all weeks that contain days from the target month. For January 2024 with Sunday as the first day of week:
- First week should start with Sunday, December 31, 2023 (or earlier if needed to complete the week)
- Last week should include all days up to and including Saturday, February 3, 2024

Currently the calendar is showing one day too late at the start and cutting off the final week.

### System Info
- @mantine/dates version: latest
- Node version: 18.x

---
Repository: /testbed
