# Bug Report

### Describe the bug

When using the date picker component, the week view is displaying incorrect dates. Instead of showing the correct start of the week based on the `firstDayOfWeek` prop, it appears to be moving forward through dates rather than backward to find the actual week start.

### Reproduction

```js
import { getStartOfWeek } from '@mantine/dates';

// Example: Get start of week for a date in the middle of the week
// Let's say we have Thursday, Jan 11, 2024 and want to find Monday (firstDayOfWeek = 1)
const result = getStartOfWeek('2024-01-11', 1);

// Expected: Should return '2024-01-08' (the Monday of that week)
// Actual: Returns a date in the future instead of going back to find the Monday
```

### Expected behavior

The function should go backward from the given date to find the start of the week. For example, if you pass in a Thursday and set `firstDayOfWeek` to Monday (1), it should return the Monday of that same week, not a future date.

### System Info

- @mantine/dates version: latest
- Browser: Chrome

This is causing calendar views to display the wrong week ranges. It seems like the logic for finding the week start is going in the wrong direction.

---
Repository: /testbed
