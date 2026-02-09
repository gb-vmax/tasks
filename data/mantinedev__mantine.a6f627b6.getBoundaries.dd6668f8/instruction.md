# Bug Report

### Describe the bug

The Heatmap component is displaying inverted color scales - cells with lower values are showing colors that should represent higher values, and vice versa. The color gradient appears to be reversed from what it should be.

### Reproduction

```js
import { Heatmap } from '@mantine/charts';

const data = {
  'cell-1': 10,
  'cell-2': 50,
  'cell-3': 100
};

<Heatmap data={data} />
```

In this example, `cell-1` (value: 10) displays with the color that should represent the maximum value, while `cell-3` (value: 100) displays with the color that should represent the minimum value.

### Expected behavior

Cells with lower numerical values should display colors from the lower end of the color scale, and cells with higher values should display colors from the upper end of the scale. The color gradient should map correctly from minimum to maximum values.

### System Info
- @mantine/charts version: latest
- Browser: Firefox 121

---
Repository: /testbed
