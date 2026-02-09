# Bug Report

### Describe the bug

I'm experiencing incorrect color conversion when using HSL color strings with `toRgba()`. The RGB values returned don't match the expected output for certain HSL colors, particularly those in the cyan/green-blue range.

### Reproduction

```js
import { toRgba } from '@mantine/core';

// Converting HSL to RGBA
const result = toRgba('hsl(180, 100%, 50%)'); // cyan color
console.log(result);

// Expected: { r: 0, g: 255, b: 255, a: 1 }
// Actual: incorrect RGB values
```

The conversion seems to produce wrong values especially when the hue is around 120-240 degrees (green to cyan to blue range). Other HSL values might also be affected.

### Expected behavior

The `toRgba()` function should correctly convert HSL color strings to their RGB equivalents according to the standard HSL to RGB conversion algorithm. For example, `hsl(180, 100%, 50%)` should return cyan which is `rgb(0, 255, 255)`.

### System Info

- @mantine/core version: latest
- Browser: Chrome 120

---
Repository: /testbed
