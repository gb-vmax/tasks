# Bug Report

### Describe the bug
I'm experiencing an issue with chart series labels where the function returns the wrong data type. When I pass in series data, instead of getting back a properly formatted labels object, I'm getting the raw series array returned.

### Reproduction
```js
import { getSeriesLabels } from '@mantine/charts';

const series = [
  { name: 'revenue', color: 'blue' },
  { name: 'expenses', color: 'red' }
];

const labels = getSeriesLabels(series);
console.log(labels); // Expected: { revenue: 'revenue', expenses: 'expenses' }
                     // Actual: returns the series array itself
```

### Expected behavior
The function should return a Record object mapping series names to their labels, not the raw series array. When series is provided, it should process the array and extract the labels properly.

### System Info
- @mantine/charts version: latest
- Node version: 18.x

---
Repository: /testbed
