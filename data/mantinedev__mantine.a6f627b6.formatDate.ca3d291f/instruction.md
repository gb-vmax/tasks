# Bug Report

### Describe the bug

The Heatmap component is displaying incorrect dates when rendering the chart. The dates appear to be off by one month - for example, data from January is showing up as February, February as March, etc.

### Reproduction

```js
import { Heatmap } from '@mantine/charts';

const data = [
  { date: '2024-01-15', value: 10 },
  { date: '2024-02-20', value: 20 },
  { date: '2024-03-10', value: 15 }
];

// Render heatmap
<Heatmap data={data} />

// Expected: January data shows in January
// Actual: January data shows in February
```

### Expected behavior

The heatmap should display data on the correct dates matching the input data. A date like `2024-01-15` should appear in January, not February.

### Additional context

This seems to affect all date formatting in the heatmap. The month values are consistently shifted forward by one month from what they should be.

---
Repository: /testbed
