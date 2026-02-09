# Bug Report

### Describe the bug

The heatmap color scale is inverted - low values are showing with colors meant for high values and vice versa. The color gradient appears to be reversed from what it should be.

### Reproduction

```jsx
import { Heatmap } from '@mantine/charts';

const data = {
  cell1: 10,
  cell2: 50,
  cell3: 90
};

// Cell with value 10 shows the color for high values
// Cell with value 90 shows the color for low values
<Heatmap data={data} />
```

When rendering a heatmap with values ranging from low to high, the colors are backwards. Cells with lower values (e.g., 10) are rendered with colors that should represent higher values, and cells with higher values (e.g., 90) get colors for lower values.

### Expected behavior

The color scale should map correctly - lower values should get colors from the lower end of the gradient, and higher values should get colors from the upper end of the gradient.

### System Info
- @mantine/charts version: latest
- Browser: Chrome

---
Repository: /testbed
