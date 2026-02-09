# Bug Report

### Color conversion producing incorrect RGB values

I'm experiencing an issue with the ColorPicker component where HSVA to RGBA conversion is producing incorrect color values. When converting certain HSV colors to RGB, the output doesn't match what I expect.

### Reproduction

```js
import { hsvaToRgbaObject } from '@mantine/core';

// Converting a pure red color (H=0, S=100%, V=100%)
const result = hsvaToRgbaObject({ h: 0, s: 1, v: 1, a: 1 });
console.log(result);
// Getting unexpected RGB values

// Also seeing issues with other hue values
const result2 = hsvaToRgbaObject({ h: 120, s: 0.5, v: 0.8, a: 1 });
console.log(result2);
// RGB output doesn't match expected green shade
```

### Expected behavior

The converter should return accurate RGB values that correspond to the input HSV color. For example:
- H=0, S=100%, V=100% should give pure red (255, 0, 0)
- H=120, S=50%, V=80% should give a proper green shade

The colors I'm getting are noticeably different from what standard HSV to RGB conversion algorithms produce.

### System Info
- @mantine/core version: latest
- Browser: Firefox 121

---
Repository: /testbed
