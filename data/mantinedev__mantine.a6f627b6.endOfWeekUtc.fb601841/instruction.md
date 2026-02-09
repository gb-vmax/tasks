# Bug Report

### Describe the bug

The Heatmap component is calculating the end of week incorrectly when the current day matches the `firstDayOfWeek` setting. This causes the date range to extend one day beyond what it should, resulting in an extra day being displayed in the heatmap.

### Reproduction

```js
import { getDatesRange } from '@mantine/charts';

// When the current date's day matches firstDayOfWeek
// For example, if firstDayOfWeek is 0 (Sunday) and today is Sunday
const date = new Date('2024-01-07'); // Sunday
const range = getDatesRange({
  date,
  firstDayOfWeek: 0,
  // ... other options
});

// The end of week calculation is off by one day
// Expected: Should end on Saturday (2024-01-13)
// Actual: Ends on Sunday (2024-01-14)
```

### Expected behavior

When `firstDayOfWeek` is set and the current date falls on that day, the week should still end 6 days later (not 7 days later). The heatmap should display exactly 7 days per week row, not 8.

### System Info
- @mantine/charts version: latest
- Browser: All browsers (UTC date calculation issue)

---
Repository: /testbed
