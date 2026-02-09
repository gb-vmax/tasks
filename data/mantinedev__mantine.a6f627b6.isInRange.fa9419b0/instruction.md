# Bug Report

### Describe the bug

I'm experiencing an issue with date range validation in the dates package. When checking if a date falls within a range, the function seems to be returning incorrect results. Dates that should be considered within the range are being excluded, and the range boundaries aren't being handled properly.

### Reproduction

```js
import { isInRange } from '@mantine/dates';

const startDate = '2024-01-01';
const endDate = '2024-01-31';
const testDate = '2024-01-15';

// This should return true since Jan 15 is between Jan 1 and Jan 31
const result = isInRange(testDate, [startDate, endDate]);
console.log(result); // Returns false (unexpected)
```

Also noticed that when the range dates are provided in reverse order (end date first, start date second), the behavior is inconsistent:

```js
// Range provided in reverse order
const result2 = isInRange('2024-01-15', ['2024-01-31', '2024-01-01']);
console.log(result2); // Should still work but doesn't
```

### Expected behavior

The `isInRange` function should correctly identify when a date falls within the provided range, regardless of the order the range boundaries are provided. A date between the start and end dates should return `true`.

### System Info

- @mantine/dates version: latest
- dayjs version: latest

---
Repository: /testbed
