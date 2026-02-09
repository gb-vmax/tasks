# Bug Report

### Describe the bug
The Heatmap component is displaying incorrect colors for data points. The color mapping seems off - values that should be mapped to specific colors in the gradient are showing different colors than expected.

### Reproduction
```js
import { Heatmap } from '@mantine/charts';

const data = [
  { x: 'A', y: 'Mon', value: 0 },
  { x: 'B', y: 'Mon', value: 50 },
  { x: 'C', y: 'Mon', value: 100 }
];

// With min=0, max=100, and a color array
<Heatmap
  data={data}
  colors={['#blue', '#yellow', '#red']}
/>
```

The middle value (50) should map to the middle color in the gradient, but it's not displaying the correct color. The color distribution across the heatmap doesn't match what you'd expect based on the min/max values.

### Expected behavior
Colors should be distributed evenly across the value range. A value halfway between min and max should get a color from the middle of the color array.

### System Info
- @mantine/charts: latest version
- React: 18.x

---
Repository: /testbed
