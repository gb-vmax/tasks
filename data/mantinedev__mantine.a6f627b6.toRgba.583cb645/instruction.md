# Bug Report

### Describe the bug

The `toRgba()` function is not correctly converting hex color values to RGBA format. When passing a valid hex color string, the function returns black (`rgb(0, 0, 0)`) with zero alpha instead of the expected color values.

### Reproduction

```js
import { toRgba } from '@mantine/core';

// This should return the correct RGB values for the hex color
const result = toRgba('#ff5733');
console.log(result);
// Expected: { r: 255, g: 87, b: 51, a: 1 }
// Actual: { r: 0, g: 0, b: 0, a: 0 }

// Same issue with shorthand hex
const result2 = toRgba('#f00');
console.log(result2);
// Expected: { r: 255, g: 0, b: 0, a: 1 }
// Actual: { r: 0, g: 0, b: 0, a: 0 }
```

### Expected behavior

When passing a hex color string to `toRgba()`, it should return an object with the correct RGB values and an alpha of 1. Instead, it's returning black with zero alpha for all hex colors.

### System Info

- @mantine/core version: latest
- Browser: Chrome 120

---
Repository: /testbed
