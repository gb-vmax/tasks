# Bug Report

### Describe the bug

After a recent update, chart series labels are not being extracted correctly. The `getSeriesLabels` function seems to be broken and returns an empty object instead of the expected label mappings.

### Reproduction

```js
import { getSeriesLabels } from '@mantine/charts';

const series = [
  { name: 'revenue', color: 'blue' },
  { name: 'expenses', color: 'red' }
];

const labels = getSeriesLabels(series);
console.log(labels);
// Expected: { revenue: 'revenue', expenses: 'expenses' }
// Actual: {}
```

### Expected behavior

The function should return a record mapping series names to their labels. Instead it's returning an empty object for all inputs.

### System Info
- @mantine/charts version: latest
- React version: 18.x

This is blocking our dashboard implementation as all chart labels are now missing. Any help would be appreciated!

---
Repository: /testbed
