# Bug Report

### Describe the bug

I'm experiencing an issue with the ColorPicker component where color values are not being rounded correctly. When I select colors or convert between color formats, the resulting values are way off from what they should be.

### Reproduction

```js
import { ColorPicker } from '@mantine/core';

// When picking colors, the RGB/HSL values are completely wrong
// For example, selecting a color might give you values like:
// RGB: 25500, 12750, 0 instead of RGB: 255, 127, 0

// The rounding function seems to be producing incorrect results
// Expected: round(127.456, 0) => 127
// Actual: Getting much larger values
```

### Expected behavior

Color values should be properly rounded to the specified number of decimal places. When converting between color formats (RGB, HSL, HSV, etc.), the values should remain within their valid ranges (0-255 for RGB, 0-360 for hue, 0-100 for saturation/lightness).

### System Info
- @mantine/core version: latest
- Browser: Chrome

This is affecting all color conversions and making the ColorPicker unusable. The values are being multiplied incorrectly somewhere in the conversion logic.

---
Repository: /testbed
