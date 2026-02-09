# Bug Report

### Describe the bug

The Heatmap component with split weeks is not rendering cells correctly. When using the split weeks view, some date cells that should be visible are not appearing, and the layout seems to be using the wrong week data.

### Reproduction

```tsx
import { Heatmap } from '@mantine/charts';

const data = [
  { date: '2024-01-01', value: 5 },
  { date: '2024-01-08', value: 3 },
  { date: '2024-01-15', value: 7 },
  // ... more dates spanning multiple months
];

// This renders with missing cells
<Heatmap
  data={data}
  splitWeeks
  // ... other props
/>
```

### Expected behavior

All date cells should render in their correct positions when using the split weeks layout. Dates should appear in the correct month columns based on their actual month value.

### System Info

- @mantine/charts version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
