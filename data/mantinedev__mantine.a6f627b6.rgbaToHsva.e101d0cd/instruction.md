# Bug Report

### Describe the bug

The ColorPicker is producing incorrect HSV values when converting from RGB colors. The saturation and hue calculations seem to be off, resulting in wrong colors being displayed or selected.

### Reproduction

```js
import { ColorPicker } from '@mantine/core';

// Try converting an RGB color to HSV
const rgbColor = { r: 100, g: 150, b: 200, a: 1 };

// When using ColorPicker with this RGB value, the displayed color
// doesn't match the expected color
<ColorPicker format="rgb" value="rgb(100, 150, 200)" />
```

When I set a specific RGB color, the picker shows a different color than expected. The hue and saturation values appear to be calculated incorrectly during the RGB to HSV conversion.

### Expected behavior

The ColorPicker should accurately convert between RGB and HSV color spaces, displaying the correct color that matches the input RGB values.

### System Info
- @mantine/core version: latest
- Browser: Chrome

---
Repository: /testbed
