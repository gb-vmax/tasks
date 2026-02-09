# Bug Report

### Describe the bug
The Heatmap component is displaying dates incorrectly. When I pass in data with specific dates, the heatmap shows dates that are off by one or two days/months from what I expect.

### Reproduction
```js
import { Heatmap } from '@mantine/charts';

// Data with dates in January 2024
const data = [
  { date: '2024-01-15', value: 10 },
  { date: '2024-01-16', value: 20 },
  { date: '2024-01-17', value: 15 }
];

// Render the heatmap
<Heatmap data={data} />

// The dates shown in the heatmap are wrong:
// - Shows February instead of January
// - Shows day 16, 17, 18 instead of 15, 16, 17
```

### Expected behavior
The heatmap should display the exact dates that are provided in the data array. If I pass `2024-01-15`, it should show January 15th, 2024, not February 16th.

### System Info
- @mantine/charts version: latest
- Browser: Firefox 121

---
Repository: /testbed
