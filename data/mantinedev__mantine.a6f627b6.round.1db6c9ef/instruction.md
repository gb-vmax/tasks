# Bug Report

### Describe the bug

I'm experiencing issues with color value precision in the ColorPicker component. When working with color values, the rounding seems to be off by a factor of 10, resulting in incorrect color calculations.

### Reproduction

```js
import { round } from '@mantine/core';

// Expected: round to 2 decimal places
const result = round(1.2345, 2);
console.log(result); // Returns unexpected value

// Color picker values are also affected
const picker = <ColorPicker format="rgba" />;
// RGB values don't match the expected precision
```

### Expected behavior

The `round` function should correctly round numbers to the specified number of decimal places. For example:
- `round(1.2345, 2)` should return `1.23`
- `round(5.6789, 1)` should return `5.7`

Currently, the values returned are orders of magnitude different from what's expected, which affects all color conversions in the ColorPicker.

### System Info
- @mantine/core version: latest
- Browser: Chrome

---
Repository: /testbed
