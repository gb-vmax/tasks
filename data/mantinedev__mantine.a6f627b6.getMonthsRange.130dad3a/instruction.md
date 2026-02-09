# Bug Report

### Describe the bug

The Heatmap component is displaying incorrect month ranges when the first day of a week is `null`. The month labels appear to be misaligned or showing the wrong month boundaries.

### Reproduction

```js
import { Heatmap } from '@mantine/charts';

const weeksData = [
  [null, '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05', '2024-01-06', '2024-01-07'],
  ['2024-01-08', '2024-01-09', '2024-01-10', '2024-01-11', '2024-01-12', '2024-01-13', '2024-01-14'],
  // ... more weeks
];

// The month range calculation is incorrect when week starts with null
```

When the first element of a week array is `null` (which can happen when the month doesn't start on the first day of the week), the month detection logic seems to be using the wrong day to determine which month the week belongs to.

### Expected behavior

The heatmap should correctly identify which month each week belongs to, even when the first day of the week is `null`. It should use the first non-null day to determine the month.

### System Info
- @mantine/charts version: latest
- Browser: Chrome

---
Repository: /testbed
