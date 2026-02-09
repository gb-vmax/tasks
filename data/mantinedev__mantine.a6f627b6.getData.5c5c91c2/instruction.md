# Bug Report

### Describe the bug

I'm experiencing an issue with the ChartTooltip component where tooltip values are not displaying correctly for certain chart types. When hovering over data points, the tooltip shows incorrect values or throws errors trying to access undefined properties.

### Reproduction

```jsx
import { AreaChart } from '@mantine/charts';

const data = [
  { date: 'Jan', value: [10, 20] },
  { date: 'Feb', value: [15, 30] },
  { date: 'Mar', value: [20, 40] }
];

function Demo() {
  return (
    <AreaChart
      h={300}
      data={data}
      dataKey="date"
      series={[{ name: 'value', color: 'blue' }]}
    />
  );
}
```

When hovering over the chart, the tooltip displays incorrect values or crashes. This seems to affect radial and scatter charts as well.

### Expected behavior

The tooltip should correctly display the calculated difference between array values for radial/scatter charts, and use the proper data key for area charts. The tooltip values should match the actual data points being hovered over.

### System Info

- @mantine/charts version: latest
- React version: 18.x

---
Repository: /testbed
