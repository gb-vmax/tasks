# Bug Report

### Describe the bug

The `MonthsList` component is displaying incorrect months when rendering the year's month grid. The months appear to be shifted by one position, starting from February instead of January.

### Reproduction

```js
import { getMonthsData } from '@mantine/dates';

const monthsData = getMonthsData('2024');
console.log(monthsData);

// Expected output:
// [
//   ['2024-01-01', '2024-02-01', '2024-03-01'],
//   ['2024-04-01', '2024-05-01', '2024-06-01'],
//   ['2024-07-01', '2024-08-01', '2024-09-01'],
//   ['2024-10-01', '2024-11-01', '2024-12-01']
// ]

// Actual output shows months starting from February
```

### Expected behavior

The months grid should start with January (month 0) and end with December (month 11), displaying all 12 months of the year in a 4x3 grid. Currently, it seems to be skipping January and including an extra month beyond December.

### System Info
- @mantine/dates version: latest
- Browser: Chrome 120

---
Repository: /testbed
