# Bug Report

### Describe the bug

The Heatmap component with `splitWeeks` is showing cells from the wrong months. When rendering a heatmap with weeks split by month, cells that should be displayed are being hidden, and the wrong weeks are being accessed from the date range.

### Reproduction

```jsx
import { Heatmap } from '@mantine/charts';

const datesRange = [
  // Week 1
  [new Date('2024-01-01'), new Date('2024-01-02'), ...],
  // Week 2
  [new Date('2024-01-08'), new Date('2024-01-09'), ...],
  // ... more weeks
];

<Heatmap
  data={myData}
  datesRange={datesRange}
  splitWeeks
  // Other props...
/>
```

The heatmap renders but cells from the correct month are not showing up. It seems like the logic for determining which cells to display based on the month is inverted, and also the week index being used doesn't match the column index.

### Expected behavior

The heatmap should display cells that belong to the current month column and hide cells from other months. Each column should access the correct week from the dates range based on its position.

### System Info
- @mantine/charts version: latest
- React version: 18.x

---
Repository: /testbed
