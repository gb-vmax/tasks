# Bug Report

### Describe the bug

The `luminance()` function is returning incorrect values for color calculations. I noticed this when working with color contrast ratios - the computed luminance values seem way off from what they should be.

### Reproduction

```js
import { luminance } from '@mantine/core';

// Testing with a standard color
const lum = luminance('rgb(128, 128, 128)');
console.log('Luminance:', lum);
// Expected: ~0.215 (standard relative luminance for mid-gray)
// Actual: incorrect value

// Also seems broken for oklch colors
const lumOklch = luminance('oklch(50% 0.1 180)');
console.log('OKLCH Luminance:', lumOklch);
// Expected: 0.5 (50% lightness normalized to 0-1 range)
// Actual: 50 (not normalized correctly)
```

### Expected behavior

The luminance function should return the correct relative luminance values according to WCAG standards (values between 0 and 1). This is critical for determining color contrast ratios for accessibility.

For oklch colors, the lightness value should be normalized to the 0-1 range.
For RGB colors, the calculation should use the proper gamma-corrected values.

### System Info

- @mantine/core version: latest
- This affects color contrast calculations and accessibility features

---
Repository: /testbed
