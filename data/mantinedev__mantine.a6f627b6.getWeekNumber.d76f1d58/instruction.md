# Bug Report

### Describe the bug

The week numbers displayed in the calendar are incorrect. It appears that the week number calculation is off by one, showing the wrong ISO week number for dates.

### Reproduction

```js
import { getWeekNumber } from '@mantine/dates';
import dayjs from 'dayjs';

// Create a week array for early January 2024
// Week should include Monday Jan 1, 2024
const week = [
  '2024-01-01', // Monday
  '2024-01-02', // Tuesday
  '2024-01-03', // Wednesday
  '2024-01-04', // Thursday
  '2024-01-05', // Friday
  '2024-01-06', // Saturday
  '2024-01-07'  // Sunday
];

const weekNumber = getWeekNumber(week);
console.log('Got week number:', weekNumber);
console.log('Expected week number:', 1); // January 1, 2024 is in ISO week 1

// The week number returned doesn't match the expected ISO week
```

### Expected behavior

The `getWeekNumber` function should return the correct ISO week number. For the week containing Monday, January 1, 2024, it should return week 1 according to the ISO 8601 standard.

### System Info
- @mantine/dates version: latest
- dayjs version: latest

---
Repository: /testbed
