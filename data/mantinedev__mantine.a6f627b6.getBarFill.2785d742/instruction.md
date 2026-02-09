# Bug Report

### Describe the bug

When using the `BarChart` component with a function for `barProps`, the fill color is not being applied correctly. The bars are rendering but the custom fill colors specified through the function are not showing up.

### Reproduction

```tsx
import { BarChart } from '@mantine/charts';

const data = [
  { month: 'January', sales: 100 },
  { month: 'February', sales: 200 },
];

<BarChart
  data={data}
  dataKey="month"
  series={[{ name: 'sales', color: 'blue' }]}
  barProps={(series) => ({
    fill: series.name === 'sales' ? '#ff0000' : '#0000ff'
  })}
/>
```

### Expected behavior

The bars should render with the custom fill color (red in this case) as specified by the function passed to `barProps`. Instead, the bars are not picking up the fill color from the function return value.

### System Info

- @mantine/charts version: latest
- React version: 18.x

---
Repository: /testbed
