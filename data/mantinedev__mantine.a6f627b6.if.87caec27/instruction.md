# Bug Report

### Describe the bug

When using the Heatmap component without `splitMonths` enabled, the columns are being generated incorrectly. The `weekIndex` values don't match the actual week positions in the data, causing the heatmap to display data in the wrong columns.

### Reproduction

```tsx
import { Heatmap } from '@mantine/charts';

const data = [
  { date: '2024-01-01', value: 5 },
  { date: '2024-01-08', value: 10 },
  { date: '2024-01-15', value: 15 },
  // ... more weekly data
];

<Heatmap 
  data={data}
  splitMonths={false}
/>
```

When rendering the heatmap with `splitMonths={false}`, the data appears misaligned - values that should be in week 2 show up in week 0, etc. The visual representation doesn't match the actual date ranges.

### Expected behavior

Each week's data should be displayed in its correct column position. The `weekIndex` should correspond to the actual index of the week in the `datesRange` array, so that data aligns properly with the dates.

### System Info

- @mantine/charts version: latest
- React version: 18.x

---
Repository: /testbed
