# Bug Report

### Describe the bug

I'm experiencing an issue with the Heatmap component where the color scale appears to be inverted. The lowest values are being colored as if they were the highest values, and vice versa. This makes the heatmap visualization completely misleading.

### Reproduction

```jsx
import { Heatmap } from '@mantine/charts';

const data = {
  'Item A': 10,
  'Item B': 50,
  'Item C': 100
};

// The heatmap displays Item A (value: 10) with the color 
// that should represent the maximum value, and Item C (value: 100)
// with the color that should represent the minimum value
<Heatmap data={data} />
```

### Expected behavior

The heatmap should use the correct color mapping where:
- Lower values get colors representing the minimum end of the scale
- Higher values get colors representing the maximum end of the scale

Currently, this mapping appears to be reversed, causing the visualization to show the opposite of what the data actually represents.

### System Info
- @mantine/charts version: latest
- Browser: Chrome

---
Repository: /testbed
