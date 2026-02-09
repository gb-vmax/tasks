# Bug Report

### Describe the bug

I'm experiencing incorrect color conversion results when using the ColorPicker component. Specifically, when converting RGB values to HSV format, the saturation values appear to be completely wrong - they're either way too high or sometimes become infinity.

### Reproduction

```js
import { ColorPicker } from '@mantine/core';

// Try converting a simple gray color
const grayColor = { r: 128, g: 128, b: 128, a: 1 };
// Expected HSV: h: 0, s: 0, v: ~50
// Actual: saturation is NaN or infinity

// Or try with a red color
const redColor = { r: 255, g: 0, b: 0, a: 1 };
// Expected HSV: h: 0, s: 100, v: 100
// Actual: saturation is way off
```

The saturation calculation seems broken - for colors that should have 0% saturation (like pure grays), I'm getting division by zero errors or infinity values. For other colors, the saturation percentage is inverted or completely incorrect.

### Expected behavior

RGB to HSV conversion should produce correct saturation values. Grays should have 0% saturation, and fully saturated colors should have 100% saturation.

### System Info

- @mantine/core version: latest
- Browser: Chrome 120

---
Repository: /testbed
