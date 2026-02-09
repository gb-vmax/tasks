# Bug Report

### Describe the bug

I'm experiencing an issue with ChartTooltip where the displayed values are incorrect for certain chart types. When hovering over radial or scatter charts with array values, the tooltip shows the sum of the values instead of the difference/range.

### Reproduction

```jsx
import { RadialBarChart } from '@mantine/charts';

const data = [
  { name: 'Item 1', value: [10, 50] }, // Should show 40 (50-10) but shows 60 (50+10)
  { name: 'Item 2', value: [20, 80] }, // Should show 60 (80-20) but shows 100 (80+20)
];

<RadialBarChart data={data} />
```

When hovering over the chart segments, the tooltip displays the sum of the array values instead of the difference. For example, `[10, 50]` shows as `60` in the tooltip when it should show `40`.

### Expected behavior

The tooltip should display the difference between the two values in the array (i.e., `value[1] - value[0]`) which represents the actual segment size/range, not the sum.

### Additional context

This seems to affect radial and scatter chart types specifically when the data values are provided as arrays with start and end points.

---
Repository: /testbed
