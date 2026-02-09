# Bug Report

### Describe the bug

Getting a runtime error when working with chart components that have no series data. The application crashes with a "Cannot read properties of null" error when trying to render charts with empty datasets.

### Reproduction

```js
import { LineChart } from '@mantine/charts';

// This causes the app to crash
<LineChart
  data={[]}
  series={[]}
  // ... other props
/>
```

Also happens when series is undefined:

```js
const chartData = {
  series: undefined
};

// Crashes when trying to render
<LineChart
  data={someData}
  series={chartData.series}
/>
```

### Expected behavior

The chart should handle empty or undefined series gracefully without throwing errors. It should either render an empty chart or show a placeholder state.

### System Info
- @mantine/charts version: latest
- React version: 18.x
- Browser: Firefox 121

This seems to have started happening recently, possibly after a recent update. Previously empty series would just render nothing without errors.

---
Repository: /testbed
