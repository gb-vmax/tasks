# Bug Report

### Describe the bug

The ChartTooltip is displaying incorrect values for radial and scatter chart types. When hovering over data points, the tooltip shows the sum of array values instead of the difference between them.

### Reproduction

```jsx
import { RadialBarChart } from '@mantine/charts';

const data = [
  { name: 'Item 1', value: [10, 50] },
  { name: 'Item 2', value: [20, 60] },
];

<RadialBarChart data={data} />
```

When hovering over the chart, the tooltip displays:
- Item 1: 60 (should be 40)
- Item 2: 80 (should be 40)

### Expected behavior

For radial and scatter charts with array values, the tooltip should display the difference between the two values (`value[1] - value[0]`), not their sum. In the example above, Item 1 should show 40 (50 - 10) and Item 2 should show 40 (60 - 20).

### Additional context

This seems to affect both radial and scatter chart types when the data values are provided as arrays with start and end points.

---
Repository: /testbed
