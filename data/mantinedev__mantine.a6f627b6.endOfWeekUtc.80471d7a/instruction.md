# Bug Report

### Describe the bug

The `endOfWeekUtc` function in the Heatmap component is calculating the end of week incorrectly. When working with dates that should return the last day of the week based on a custom `firstDayOfWeek` setting, the function returns the wrong date.

### Reproduction

```js
// Assuming firstDayOfWeek is set to 1 (Monday)
const date = new Date('2024-01-10T00:00:00Z'); // Wednesday
const endOfWeek = endOfWeekUtc(date, 1);

// Expected: Should return Sunday (2024-01-14)
// Actual: Returns incorrect date
```

The calculation for determining how many days to add to reach the end of the week appears to be off. This affects any heatmap visualization that relies on weekly groupings with a custom first day of week.

### Expected behavior

The function should correctly calculate the last day of the week (6 days after the first day of week) regardless of what day of the week the input date falls on.

### System Info
- @mantine/charts version: latest
- Browser: N/A (affects all environments)

---
Repository: /testbed
