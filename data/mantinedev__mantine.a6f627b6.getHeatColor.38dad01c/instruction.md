# Bug Report

### Describe the bug

The heatmap color calculation seems to be inverted - higher values are showing cooler colors and lower values are showing warmer colors. This is the opposite of what you'd expect from a typical heatmap visualization.

### Reproduction

```js
import { getHeatColor } from '@mantine/charts';

const colors = ['#blue', '#yellow', '#orange', '#red'];

// With a value close to max, expecting a warm color (red)
const result1 = getHeatColor({
  value: 90,
  min: 0,
  max: 100,
  colors
});
console.log(result1); // Returns blue instead of red

// With a value close to min, expecting a cool color (blue)
const result2 = getHeatColor({
  value: 10,
  min: 0,
  max: 100,
  colors
});
console.log(result2); // Returns red instead of blue
```

### Expected behavior

Higher values should map to warmer colors (end of the color array) and lower values should map to cooler colors (start of the color array). In the example above:
- value=90 should return a color near the end of the array (red/orange)
- value=10 should return a color near the start of the array (blue)

### System Info
- @mantine/charts version: latest
- Browser: Chrome

---
Repository: /testbed
