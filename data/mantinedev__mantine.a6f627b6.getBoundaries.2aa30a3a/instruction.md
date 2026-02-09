# Bug Report

### Describe the bug
The Heatmap component is not calculating boundaries correctly when no domain is provided. Instead of using the actual data values to determine min/max boundaries, it appears to be using something else entirely, resulting in incorrect visualization ranges.

### Reproduction
```tsx
import { Heatmap } from '@mantine/charts';

const data = {
  'A': 10,
  'B': 25,
  'C': 15,
  'D': 30
};

// Without explicit domain, boundaries should be [10, 30]
// But the heatmap displays with incorrect color scaling
<Heatmap data={data} />
```

### Expected behavior
When domain is not explicitly provided, the component should automatically calculate boundaries based on the minimum and maximum values in the data object. For the example above, it should use `[10, 30]` as the boundaries.

### Actual behavior
The heatmap renders with incorrect boundaries, causing the color scale to not properly represent the data values.

### System Info
- @mantine/charts version: latest
- React version: 18.x

---
Repository: /testbed
