# Bug Report

### Describe the bug
The week number calculation in the Month component is returning incorrect values. When displaying a calendar with week numbers enabled, the numbers shown don't match the expected ISO week numbers.

### Reproduction
```js
import { Month } from '@mantine/dates';

// Display a month with week numbers enabled
<Month 
  withWeekNumbers 
  month={new Date(2024, 0, 1)} // January 2024
/>
```

The week numbers displayed are off and don't align with the standard ISO 8601 week numbering system. For example, weeks that should be numbered according to ISO standards (where week 1 contains the first Thursday of the year) are showing different numbers.

### Expected behavior
Week numbers should follow the ISO 8601 standard where:
- Week 1 is the week containing the first Thursday of the year
- Weeks start on Monday
- The displayed week numbers should match what you'd see in standard calendar applications

### System Info
- @mantine/dates version: latest
- Browser: Chrome

---
Repository: /testbed
