# Bug Report

### Describe the bug

I'm experiencing an issue with color parsing when using `rgba()` or `rgb()` color strings that contain decimal values. When I pass colors like `rgba(255, 128, 0, 0.5)` or `rgb(100.5, 200.3, 150.7)`, the decimal points are being stripped out and the colors are rendered incorrectly.

### Reproduction

```js
import { toRgba } from '@mantine/core';

// This doesn't work correctly - decimal point is removed
const color1 = toRgba('rgba(255, 128, 0, 0.5)');
// Expected: { r: 255, g: 128, b: 0, a: 0.5 }
// Actual: { r: 255, g: 128, b: 0, a: 05 } (decimal point removed)

// Same issue with rgb values that have decimals
const color2 = toRgba('rgb(100.5, 200.3, 150.7)');
// Expected: { r: 100.5, g: 200.3, b: 150.7, a: 1 }
// Actual: Values parsed incorrectly without decimal points
```

### Expected behavior

The function should properly parse decimal values in RGB/RGBA color strings. Decimal points should not be stripped from the numeric values during parsing.

### System Info

- @mantine/core version: latest
- Browser: Chrome/Firefox

---
Repository: /testbed
