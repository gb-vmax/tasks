# Bug Report

### Describe the bug

When using `toRgba()` with RGB/RGBA color strings that contain decimal values, the function fails to parse them correctly. Colors with decimal opacity values or decimal RGB components are not being converted properly.

### Reproduction

```js
import { toRgba } from '@mantine/core';

// This doesn't work correctly
const result = toRgba('rgba(255, 128, 64, 0.5)');
// Expected: { r: 255, g: 128, b: 64, a: 0.5 }
// Actual: Incorrect parsing due to decimal point being stripped

// Also affects rgb strings with decimals
const result2 = toRgba('rgb(127.5, 64.2, 32.8)');
// Decimal values are not parsed correctly
```

### Expected behavior

The `toRgba()` function should correctly handle RGB/RGBA color strings that contain decimal values in either the color components or the alpha channel. Decimal points should be preserved during parsing.

### System Info
- @mantine/core version: latest
- Browser: Chrome

---
Repository: /testbed
