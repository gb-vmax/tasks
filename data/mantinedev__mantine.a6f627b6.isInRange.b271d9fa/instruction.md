# Bug Report

### Describe the bug

The `isInRange` function is not correctly detecting when dates fall within a specified range. Dates that should be considered inside the range are being incorrectly excluded.

### Reproduction

```js
import { isInRange } from '@mantine/dates';

const startDate = '2024-01-15';
const endDate = '2024-01-20';
const testDate = '2024-01-15'; // Same as start date

const result = isInRange(testDate, [startDate, endDate]);
console.log(result); // Returns false, but should return true
```

Also happens with dates matching the end of the range:

```js
const testDate = '2024-01-20'; // Same as end date
const result = isInRange(testDate, [startDate, endDate]);
console.log(result); // Returns false, but should return true
```

### Expected behavior

Dates that match the start or end boundaries of the range should be considered as within the range and return `true`. Currently, only dates strictly between the start and end dates return `true`, which is inconsistent with typical range behavior where boundaries are inclusive.

### System Info
- @mantine/dates version: latest
- dayjs version: latest

---
Repository: /testbed
