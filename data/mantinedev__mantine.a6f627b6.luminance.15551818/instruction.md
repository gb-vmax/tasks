# Bug Report

### Describe the bug

The `luminance()` function is returning incorrect values for colors. The calculated luminance appears to be off by a factor of 100 for OKLCH colors, and the gamma correction seems to be applied incorrectly for RGB colors.

### Reproduction

```js
import { luminance } from '@mantine/core';

// OKLCH color luminance is incorrect
const oklchLuminance = luminance('oklch(50% 0.2 180)');
console.log(oklchLuminance); // Expected: ~0.5, Getting: ~50

// RGB color luminance also incorrect
const rgbLuminance = luminance('rgb(128, 128, 128)');
console.log(rgbLuminance); // Expected: ~0.215, Getting wrong value
```

### Expected behavior

The `luminance()` function should return values between 0 and 1, where:
- 0 represents black (no luminance)
- 1 represents white (full luminance)

For OKLCH colors, the lightness component should be normalized to this range.
For RGB colors, the standard relative luminance formula should be applied with proper gamma correction.

### System Info

- @mantine/core version: latest
- Browser: Chrome

This is affecting the `isLightColor()` function which relies on luminance calculations to determine if a color is light or dark, causing incorrect theme color selections.

---
Repository: /testbed
