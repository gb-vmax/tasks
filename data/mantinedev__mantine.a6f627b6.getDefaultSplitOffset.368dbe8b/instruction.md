# Bug Report

### Describe the bug

The AreaChart component crashes when trying to render with split mode enabled. Getting an error that `getDefaultSplitOffset` is not a function.

### Reproduction

```jsx
import { AreaChart } from '@mantine/charts';

const data = [
  { date: 'Jan', value: 100 },
  { date: 'Feb', value: 200 },
  { date: 'Mar', value: 150 }
];

function Demo() {
  return (
    <AreaChart
      data={data}
      series={[{ name: 'value', color: 'blue' }]}
      splitColors={['red', 'green']}
      splitOffset="auto"
    />
  );
}
```

### Expected behavior

The chart should render properly with the split visualization applied at the default offset when using a single series.

### System Info
- @mantine/charts version: latest
- React version: 18.x
- Browser: Chrome 121

---
Repository: /testbed
