# Bug Report

### Describe the bug

The Heatmap component is generating incorrect date ranges. When creating a heatmap with a date range, the dates are being calculated incorrectly, causing the chart to display data for the wrong days.

### Reproduction

```js
import { Heatmap } from '@mantine/charts';

// Create a heatmap with data spanning multiple days
const data = [
  { date: '2024-01-01', value: 10 },
  { date: '2024-01-02', value: 20 },
  { date: '2024-01-03', value: 15 },
  // ... more dates
];

// The heatmap displays dates that don't match the input data
<Heatmap data={data} />
```

After rendering, the dates shown in the heatmap don't align with the actual dates in the data. For example, if I have data for January 1-7, the heatmap might show dates that are off by several days.

### Expected behavior

The heatmap should correctly calculate and display the date range based on the input data. Each cell should correspond to the correct date.

### System Info

- @mantine/charts version: latest
- Browser: Chrome 120

---
Repository: /testbed
