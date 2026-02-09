# Bug Report

### Describe the bug

I'm experiencing issues with HSL to RGBA color conversion in Mantine. When converting HSL color strings to RGBA format, the resulting colors are completely incorrect. The RGB values seem way off from what they should be.

### Reproduction

```js
import { toRgba } from '@mantine/core';

// Try converting an HSL color
const color1 = toRgba('hsl(240, 100%, 50%)'); // Should be pure blue
console.log(color1); // Getting wrong RGB values

const color2 = toRgba('hsl(0, 50%, 50%)'); // Should be a muted red
console.log(color2); // Also incorrect

// The saturation calculation seems broken
const color3 = toRgba('hsl(120, 80%, 60%)'); // Green with high saturation
console.log(color3); // Colors don't match expected output
```

### Expected behavior

HSL colors should convert accurately to their RGBA equivalents. For example:
- `hsl(240, 100%, 50%)` should produce RGB values close to (0, 0, 255) for pure blue
- `hsl(0, 50%, 50%)` should produce a proper muted red
- Colors with different hue ranges should all convert correctly

### System Info

- @mantine/core version: latest
- Browser: Chrome 121

The conversion was working fine in previous versions but seems broken now. This affects any component that relies on HSL color input.

---
Repository: /testbed
