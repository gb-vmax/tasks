# Bug Report

### Describe the bug

The `isInRange` function is not correctly identifying dates that fall within a given date range. When checking if a date is within a range, dates that should be considered "in range" are being returned as false, and dates outside the range are sometimes returned as true.

### Reproduction

```js
import { isInRange } from '@mantine/dates';

const startDate = '2024-01-10';
const endDate = '2024-01-20';
const testDate = '2024-01-15';

// This should return true but returns false
const result = isInRange(testDate, [startDate, endDate]);
console.log(result); // Expected: true, Actual: false

// Also fails when range is provided in reverse order
const result2 = isInRange(testDate, [endDate, startDate]);
console.log(result2); // Expected: true, Actual: false
```

### Expected behavior

Dates that fall within the specified range (inclusive of start and end dates) should return `true`. Dates outside the range should return `false`. The function should handle ranges provided in any order (start-end or end-start).

### System Info

- @mantine/dates version: latest
- Browser: Chrome 120

---
Repository: /testbed
