# Bug Report

### Describe the bug

The calendar month view is rendering an incorrect number of days. When displaying a month, the calendar should show 35 days (5 weeks) but it's currently showing 42 days (6 weeks) instead.

### Reproduction

```jsx
import { Calendar } from '@mantine/dates';

// Render a calendar for April 2022
<Calendar defaultDate={new Date(2022, 3, 15)} />
```

When rendering the calendar:
- Expected: 35 day cells (5 weeks of 7 days)
- Actual: 42 day cells (6 weeks of 7 days)

The day indices are also off - for example, the selected date (15th of April) appears at index 14 instead of the expected index 18.

### Additional context

This also affects the outside dates rendering. The last day of April (30th) is now appearing at index 34 instead of index 33, and the behavior when clicking on outside dates has changed (click handler is being called twice instead of once).

### System Info
- @mantine/dates: latest
- React version: 18.x

---
Repository: /testbed
