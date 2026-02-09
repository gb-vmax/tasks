# Bug Report

### Describe the bug

I'm encountering an issue with color parsing when using RGB/RGBA color strings with decimal values. When I pass a color string like `rgb(255, 128, 0.5)` or any RGB color with a decimal point in one of the color channel values, the parsing fails and returns incorrect values.

### Reproduction

```js
import { toRgba } from '@mantine/core';

// This returns incorrect values - decimal points in color channels are being stripped
const color1 = toRgba('rgb(255, 128, 0.5)');
console.log(color1); // Expected: { r: 255, g: 128, b: 0.5, a: 1 }

// Similar issue with other decimal values in RGB channels
const color2 = toRgba('rgb(100.5, 200.7, 50.3)');
console.log(color2); // Decimal points are removed from the values
```

### Expected behavior

The function should correctly parse RGB color strings that contain decimal values in the color channels. Decimal points (`.`) should be preserved when parsing the numeric values, not stripped out during the regex replacement.

### System Info

- @mantine/core version: latest
- Browser: Chrome 120

---
Repository: /testbed
