# Bug Report

### Describe the bug

I'm experiencing an issue with the Heatmap component where the week indices are not being set correctly when `splitMonths` is disabled. Instead of getting sequential week numbers (0, 1, 2, 3...), all weeks are being assigned the same index value that corresponds to the month number.

### Reproduction

```js
import { Heatmap } from '@mantine/charts';

// Create a heatmap with splitMonths disabled
const data = [
  { date: '2024-01-01', value: 5 },
  { date: '2024-01-08', value: 3 },
  { date: '2024-01-15', value: 7 },
  { date: '2024-01-22', value: 2 },
];

<Heatmap 
  data={data}
  splitMonths={false}
/>

// Expected: weeks should have indices 0, 1, 2, 3
// Actual: all weeks have the same index (the month number)
```

### Expected behavior

When `splitMonths` is set to `false`, each week should have a unique sequential index (0, 1, 2, 3, etc.) representing its position in the date range. Currently, it appears all weeks are getting assigned the month number instead of their actual week index.

This causes issues with rendering and positioning of the heatmap cells, as multiple weeks end up with identical indices.

### System Info
- @mantine/charts version: latest
- Browser: Chrome

---
Repository: /testbed
