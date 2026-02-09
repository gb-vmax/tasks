# Bug Report

### Describe the bug

I'm having an issue with the chart legend where items that should be hidden are now showing up, and items that should be visible are being filtered out. It seems like the legend filtering logic is inverted.

### Reproduction

```jsx
import { LineChart } from '@mantine/charts';

const data = [
  { date: 'Jan', value1: 100, value2: 200 },
  { date: 'Feb', value1: 150, value2: 250 },
];

// When rendering a chart with legend items
<LineChart
  data={data}
  dataKey="date"
  series={[
    { name: 'value1', color: 'blue' },
    { name: 'value2', color: 'none' }, // This should be hidden
  ]}
/>
```

### Expected behavior

Legend items with `color: 'none'` should be filtered out and not displayed in the legend. Currently, it appears that only items with `color: 'none'` are being shown, while all other items are being hidden. The filtering behavior seems to be backwards.

### System Info

- @mantine/charts version: latest
- React version: 18.x

---
Repository: /testbed
