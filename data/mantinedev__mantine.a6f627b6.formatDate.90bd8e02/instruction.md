# Bug Report

### Describe the bug

The Heatmap component is displaying incorrect dates. When I pass data with specific dates, the dates shown in the heatmap are off by one month and the day values appear to be incorrectly padded.

### Reproduction

```js
import { Heatmap } from '@mantine/charts';

const data = [
  { date: '2024-01-15', value: 10 },
  { date: '2024-02-20', value: 15 },
  { date: '2024-03-05', value: 8 }
];

// Expected: Dates should display as 2024-01-15, 2024-02-20, 2024-03-05
// Actual: Dates are showing as 2024-02-15, 2024-03-20, 2024-04-05
<Heatmap data={data} />
```

When I hover over the heatmap cells or check the tooltip, the dates are shifted forward by one month. For example, data for January 15th is being displayed as February 15th.

Additionally, I noticed that days with leading zeros (like day 01, 02, etc.) are being displayed with incorrect padding - they show as "11", "12" instead of "01", "02".

### Expected behavior

The heatmap should display the exact dates that are provided in the data array without any month offset or incorrect day padding.

### System Info
- @mantine/charts version: latest
- Browser: Chrome 121

---
Repository: /testbed
