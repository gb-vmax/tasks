# Bug Report

### Describe the bug

When using date clamping with `minDate` and `maxDate`, the default date is not being clamped correctly. The date picker seems to be returning the wrong date when the current date falls outside the allowed range.

### Reproduction

```js
import { getDefaultClampedDate } from '@mantine/dates';

// Case 1: Current date is before minDate
const result1 = getDefaultClampedDate({
  minDate: new Date('2024-01-15'),
  maxDate: new Date('2024-12-31'),
  timezone: 'UTC'
});
// Expected: Should return minDate (2024-01-15) if today is before it
// Actual: Returns today's date even when it's before minDate

// Case 2: Current date is after maxDate
const result2 = getDefaultClampedDate({
  minDate: new Date('2023-01-01'),
  maxDate: new Date('2023-12-31'),
  timezone: 'UTC'
});
// Expected: Should return maxDate (2023-12-31) if today is after it
// Actual: Returns today's date even when it's after maxDate
```

### Expected behavior

When the current date is outside the `minDate`/`maxDate` range, the function should return the closest valid date (either `minDate` or `maxDate`). Instead, it appears to be returning the current date regardless of the constraints.

### System Info

- @mantine/dates version: latest
- Browser: Chrome 120

---
Repository: /testbed
