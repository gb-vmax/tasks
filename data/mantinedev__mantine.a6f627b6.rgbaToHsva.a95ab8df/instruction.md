# Bug Report

### Describe the bug

I'm experiencing incorrect color conversions when using the ColorPicker component. When converting RGB colors to HSV format, the saturation and hue values are calculated incorrectly, resulting in colors that don't match the original input.

### Reproduction

```js
import { ColorPicker } from '@mantine/core';

// Try converting a specific RGB color
const color = { r: 128, g: 128, b: 255, a: 1 };

// When the ColorPicker processes this color internally,
// the HSV conversion produces wrong saturation values
// Expected HSV: h: 240, s: 50, v: 100
// Actual result: saturation is off by a noticeable margin
```

The issue seems to affect colors across the spectrum, but is particularly noticeable with:
- Colors where green component equals the max value
- Mid-range saturation colors

### Expected behavior

The ColorPicker should accurately convert between RGB and HSV color spaces. When I input an RGB value and the component converts it to HSV internally, selecting the same visual color should produce the same RGB output.

Currently, there's a visible drift in color values after conversion, especially noticeable when working with blues and purples.

### System Info
- @mantine/core version: latest
- Browser: Chrome/Firefox (affects both)

---
Repository: /testbed
