# Bug Report

### Describe the bug

The `isInRange` function is not correctly detecting dates that fall within a specified date range. Dates that should be included in the range are being excluded, and the range boundaries are not being handled properly.

### Reproduction

```js
import { isInRange } from '@mantine/dates';

const startDate = '2024-01-01';
const endDate = '2024-01-31';
const testDate = '2024-01-15';

// This should return true but returns false
const result = isInRange(testDate, [startDate, endDate]);
console.log(result); // Expected: true, Actual: false
```

Also, when passing the range in reverse order:

```js
const result2 = isInRange(testDate, [endDate, startDate]);
console.log(result2); // Also returns false when it should be true
```

### Expected behavior

The function should correctly identify when a date falls within the provided range, regardless of the order the range boundaries are provided. Dates at the start and end of the range should also be properly included.

### System Info
- @mantine/dates version: latest
- dayjs version: latest

---
Repository: /testbed
