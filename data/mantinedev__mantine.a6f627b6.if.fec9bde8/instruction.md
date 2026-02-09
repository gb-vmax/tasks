# Bug Report

### Describe the bug

The heatmap component is not rendering month boundaries correctly. When displaying data across multiple months, the column grouping appears broken and months are not being separated properly in the visualization.

### Reproduction

```js
import { Heatmap } from '@mantine/charts';

// Create heatmap data spanning multiple months
const data = [
  { date: '2024-01-15', value: 10 },
  { date: '2024-02-20', value: 15 },
  { date: '2024-03-10', value: 20 },
];

<Heatmap data={data} />
```

When the heatmap renders, the month boundaries are not detected and columns are not grouped correctly. It seems like the logic for identifying when a new month starts is not working as expected.

### Expected behavior

The heatmap should properly identify month boundaries and group columns accordingly, showing clear separation between different months in the visualization.

### System Info
- @mantine/charts version: latest
- Browser: Chrome

---
Repository: /testbed
