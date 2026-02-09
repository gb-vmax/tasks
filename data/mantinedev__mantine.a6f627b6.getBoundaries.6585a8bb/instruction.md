# Bug Report

### Heatmap color scale appears inverted

I'm experiencing an issue with the Heatmap component where the color scale seems to be backwards. Low values are getting colors that should be assigned to high values, and vice versa.

### Reproduction

```tsx
import { Heatmap } from '@mantine/charts';

const data = {
  'Jan': 10,
  'Feb': 50,
  'Mar': 90
};

<Heatmap data={data} />
```

In this example, January (value 10) is showing up with the color that should represent high values, while March (value 90) is showing the color for low values. The gradient is completely reversed from what it should be.

This also happens when I explicitly provide a domain:

```tsx
<Heatmap data={data} domain={[0, 100]} />
```

The colors are still inverted - 0 gets the color for 100, and 100 gets the color for 0.

### Expected behavior

Low values should map to one end of the color scale and high values to the other end. The color gradient should increase consistently with the data values, not in reverse.

### System Info
- @mantine/charts: latest version
- React: 18.x

---
Repository: /testbed
