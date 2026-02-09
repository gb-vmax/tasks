# Bug Report

### Describe the bug
The `luminance()` function is returning incorrect values for color brightness calculations. This affects the `isLightColor()` function and any components that rely on automatic text color contrast adjustments.

### Reproduction
```js
import { luminance } from '@mantine/core';

// Testing with a red color
const redLuminance = luminance('rgb(255, 0, 0)');
console.log('Red luminance:', redLuminance);
// Expected: ~0.2126 (red should have higher luminance value)
// Actual: ~0.0722 (incorrect, too low)

// Testing with blue color
const blueLuminance = luminance('rgb(0, 0, 255)');
console.log('Blue luminance:', blueLuminance);
// Expected: ~0.0722 (blue should have lower luminance value)
// Actual: ~0.2126 (incorrect, too high)

// Also affects oklch colors
const oklchColor = 'oklch(50% 0.2 180)';
const oklchLuminance = luminance(oklchColor);
console.log('OKLCH luminance:', oklchLuminance);
// Expected: 0.5 (50% lightness = 0.5)
// Actual: ~0.196 (incorrect calculation)
```

### Expected behavior
The luminance function should correctly calculate relative luminance values according to the standard formula where red has the highest weight (0.2126), green is middle (0.7152), and blue is lowest (0.0722). For OKLCH colors, the lightness value should be divided by 100 to get a 0-1 range.

This is causing issues with automatic text color selection on colored backgrounds - light backgrounds are being treated as dark and vice versa.

### System Info
- @mantine/core version: latest
- Browser: All browsers affected

---
Repository: /testbed
