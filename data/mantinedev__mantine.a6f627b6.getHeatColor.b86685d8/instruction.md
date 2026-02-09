# Bug Report

### Describe the bug

The Heatmap component is not assigning colors correctly to values. When I have a range of values, the color distribution seems off - the highest values are getting intermediate colors instead of the maximum color from the color scale.

### Reproduction

```js
import { Heatmap } from '@mantine/charts';

const data = [
  { value: 0 },
  { value: 5 },
  { value: 10 }
];

const colors = ['#blue', '#yellow', '#red'];

// With min=0, max=10, value=10 should get '#red' (the last color)
// But it's getting an intermediate color instead
<Heatmap 
  data={data}
  colors={colors}
/>
```

When the maximum value (10) is passed, I expect it to receive the last color in the array ('#red'), but it's not working as expected. The color mapping seems to be shifted or calculated incorrectly.

### Expected behavior

- Value at minimum (0) should get the first color
- Value at maximum (10) should get the last color  
- Values in between should be distributed proportionally across the color range

### System Info
- @mantine/charts version: latest
- Browser: Chrome

---
Repository: /testbed
