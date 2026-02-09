# Bug Report

### Describe the bug

The ColorPicker component is producing incorrect HSV color values when converting from RGB. The hue and saturation calculations appear to be completely wrong, resulting in colors displaying differently than expected.

### Reproduction

```js
import { ColorPicker } from '@mantine/core';

// Try converting a red color
const redRgb = { r: 255, g: 0, b: 0, a: 1 };
// Expected HSV: h: 0, s: 100, v: 100
// Actual result: incorrect hue and saturation values

// The color picker shows the wrong color when initialized with RGB values
<ColorPicker format="rgb" value="rgb(255, 0, 0)" />
```

When I set a color using RGB format, the color picker displays a completely different color than what was specified. For example, setting pure red (255, 0, 0) results in an incorrect color being shown in the picker.

### Expected behavior

RGB to HSV conversion should produce accurate hue and saturation values. Pure red (255, 0, 0) should convert to HSV values of h: 0, s: 100, v: 100.

### System Info
- @mantine/core version: latest
- Browser: Chrome 120

---
Repository: /testbed
