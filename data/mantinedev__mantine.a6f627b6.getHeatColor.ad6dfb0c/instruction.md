# Bug Report

### Describe the bug

The heatmap color calculation seems off - colors are not being distributed correctly across the value range. When I have a dataset with values from min to max, the color mapping appears skewed and doesn't match the expected gradient distribution.

### Reproduction

```js
import { getHeatColor } from '@mantine/charts';

const colors = ['blue', 'yellow', 'red'];

// Test with a simple range
const result1 = getHeatColor({
  value: 0,
  min: 0,
  max: 10,
  colors
});

const result2 = getHeatColor({
  value: 5,
  min: 0,
  max: 10,
  colors
});

const result3 = getHeatColor({
  value: 10,
  min: 0,
  max: 10,
  colors
});

// The color distribution doesn't look right
console.log(result1, result2, result3);
```

### Expected behavior

The colors should be evenly distributed across the value range. For a 3-color gradient from 0 to 10:
- Values near 0 should get the first color
- Values near 5 should get the middle color  
- Values near 10 should get the last color

Instead, the mapping seems incorrect and values that should be in the middle of the range are getting colors from the wrong part of the gradient.

### System Info
- @mantine/charts version: latest
- Browser: Chrome

---
Repository: /testbed
