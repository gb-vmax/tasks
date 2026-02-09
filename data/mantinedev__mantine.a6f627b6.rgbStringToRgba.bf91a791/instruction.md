# Bug Report

### Describe the bug

I'm experiencing an issue with color parsing when using rgba strings with the `/` separator (CSS Color Level 4 syntax). The alpha channel value is being set incorrectly - it appears to always default to 1 regardless of the actual alpha value specified.

### Reproduction

```js
import { toRgba } from '@mantine/core';

// Using CSS Color Level 4 syntax with / separator
const color1 = toRgba('rgb(255 0 0 / 0.5)');
console.log(color1);
// Expected: { r: 255, g: 0, b: 0, a: 0.5 }
// Actual: { r: 255, g: 0, b: 0, a: 1 }

const color2 = toRgba('rgba(100 150 200 / 0.3)');
console.log(color2);
// Expected: { r: 100, g: 150, b: 200, a: 0.3 }
// Actual: { r: 100, g: 150, b: 200, a: 1 }
```

### Expected behavior

When parsing rgba/rgb color strings with the forward slash separator (modern CSS syntax), the alpha channel should be correctly extracted and returned. Colors with alpha values less than 1 should maintain their transparency.

### System Info

- @mantine/core version: latest
- Browser: Chrome/Firefox (affects all browsers)

---
Repository: /testbed
