# Bug Report

### Describe the bug

The ColorPicker component is producing incorrect HSV/HSLA color values when converting from RGB. The hue calculation seems to be off, particularly for grayscale colors and certain edge cases.

### Reproduction

```js
import { parseHsla } from '@mantine/core';

// Test with a grayscale color
const gray = parseHsla('rgb(128, 128, 128)');
console.log(gray.h); // Expected: 0, but getting unexpected value

// Test with pure red
const red = parseHsla('rgb(255, 0, 0)');
console.log(red.h); // Expected: 0, but getting incorrect hue

// The saturation values also seem wrong for some colors
console.log(gray.s); // Should be 0 for grayscale
```

When converting RGB colors to HSV/HSLA format, the resulting hue and saturation values don't match what they should be. This is especially noticeable with:
- Grayscale colors (should have 0 saturation)
- Pure primary colors (red, green, blue)
- Colors where R=G=B

### Expected behavior

The color conversion should produce accurate HSV/HSLA values that match standard color space transformations. Grayscale colors should have 0 saturation, and hue calculations should be consistent with the standard RGB to HSV conversion algorithm.

### System Info
- @mantine/core version: latest
- Browser: All browsers affected

---
Repository: /testbed
