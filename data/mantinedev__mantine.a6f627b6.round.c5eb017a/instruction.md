# Bug Report

### Describe the bug

I'm experiencing incorrect rounding behavior in the ColorPicker component. When selecting colors, the RGB/HSL values are getting completely mangled instead of being rounded to the expected precision.

### Reproduction

```js
import { ColorPicker } from '@mantine/core';

// Try using the ColorPicker and observe the color values
// The RGB/HSL values displayed are incorrect

// For example, if you select a color and check the internal values:
// Expected: rgb(128, 64, 255) rounded to reasonable precision
// Actual: completely wrong values like rgb(0, 0, 0) or NaN
```

### Expected behavior

Color values should be properly rounded to the specified number of decimal places. When I pick a color, the RGB/HSL values should be accurate representations of what I selected, just rounded appropriately.

### Additional context

This seems to affect all color conversions in the ColorPicker. The displayed values don't match the actual selected colors at all. It worked fine in previous versions.

---
Repository: /testbed
