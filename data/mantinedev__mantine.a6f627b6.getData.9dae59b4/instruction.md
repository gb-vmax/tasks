# Bug Report

### Describe the bug

I'm experiencing an issue with the ChartTooltip component where the displayed values appear to be incorrect or inverted. When hovering over chart elements (particularly radial and scatter charts), the tooltip shows unexpected values that don't match what's actually being displayed on the chart.

### Reproduction

```jsx
import { RadialBarChart } from '@mantine/charts';

const data = [
  { name: 'Category A', value: [10, 50] },
  { name: 'Category B', value: [20, 60] }
];

<RadialBarChart data={data} />
```

When hovering over the chart, the tooltip displays values that seem inverted or calculated incorrectly. For example, instead of showing the difference as `50 - 10 = 40`, it appears to show `10 - 50 = -40`.

### Expected behavior

The tooltip should display the correct calculated values based on the chart data. For array values, it should compute the difference in the proper order (upper bound minus lower bound).

### System Info
- @mantine/charts version: latest
- Browser: Chrome 120

Has anyone else encountered this? The values in the tooltip don't seem to match what's visually represented in the chart.

---
Repository: /testbed
