# Bug Report

### Describe the bug

The Heatmap component is generating incorrect date strings when using the dates range functionality. The dates appear to be off by one day and the month values don't match the expected UTC format.

### Reproduction

```js
import { Heatmap } from '@mantine/charts';

// When rendering a heatmap with date-based data
const data = [
  { date: '2024-01-15', value: 10 },
  { date: '2024-01-16', value: 20 }
];

// The dates displayed in the heatmap don't match the input dates
// For example, '2024-01-15' might show as '2024-01-16' or with wrong month
```

### Expected behavior

The heatmap should display dates exactly as they are provided in the data array. If the input date is `2024-01-15`, the heatmap should show `2024-01-15`, not a different date.

### System Info
- @mantine/charts version: latest
- Browser: Chrome 120

---
Repository: /testbed
