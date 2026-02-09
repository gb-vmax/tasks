# Bug Report

### Describe the bug

The heatmap color scaling is reversed - higher values are showing cooler colors and lower values are showing warmer colors. Additionally, the color assignment seems off by one index.

### Reproduction

```js
import { getHeatColor } from '@mantine/charts';

const colors = ['blue', 'yellow', 'orange', 'red'];

// Minimum value should get the first color (blue)
const minColor = getHeatColor({ value: 0, min: 0, max: 100, colors });
console.log(minColor); // Expected: 'blue', but gets a different color

// Maximum value should get the last color (red)
const maxColor = getHeatColor({ value: 100, min: 0, max: 100, colors });
console.log(maxColor); // Expected: 'red', but gets 'blue' instead

// Mid-range value
const midColor = getHeatColor({ value: 50, min: 0, max: 100, colors });
console.log(midColor); // Color gradient is inverted
```

### Expected behavior

- Minimum values should map to the first color in the array
- Maximum values should map to the last color in the array
- The color gradient should progress naturally from min to max following the color array order

### System Info

- @mantine/charts version: latest
- Browser: Chrome 120

---
Repository: /testbed
