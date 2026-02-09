# Bug Report

### Describe the bug

The `luminance()` function is returning incorrect values for color calculations. When I test it with various colors, the luminance values seem way off from what they should be.

### Reproduction

```js
import { luminance, isLightColor } from '@mantine/core';

// Testing with a standard color
const lum = luminance('#ffffff'); // white
console.log(lum); // Expected: ~1.0, but getting incorrect value

// This also affects isLightColor detection
const isLight = isLightColor('#888888'); // mid-gray
console.log(isLight); // Getting wrong result
```

For OKLCH colors, the values are also completely wrong:

```js
const oklchLum = luminance('oklch(0.5 0.1 180)');
console.log(oklchLum); // Should be around 0.5, but getting 50
```

### Expected behavior

The luminance function should return values between 0 and 1, where 0 is black and 1 is white. This is the standard range for relative luminance calculations used in WCAG contrast ratio formulas.

The current implementation seems to be calculating luminance incorrectly, which breaks color contrast detection and any components that rely on determining if a color is light or dark.

### System Info
- @mantine/core version: latest
- Browser: Chrome 120

---
Repository: /testbed
