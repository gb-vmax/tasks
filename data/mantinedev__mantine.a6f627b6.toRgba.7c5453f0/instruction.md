# Bug Report

### Describe the bug

I'm experiencing an issue with color conversion when using `rgb()` format colors. It seems like the library is no longer recognizing `rgb()` color strings properly and they're not being converted to RGBA format.

### Reproduction

```js
import { toRgba } from '@mantine/core';

// This doesn't work anymore
const result = toRgba('rgb(255, 0, 0)');
console.log(result); // Expected: { r: 255, g: 0, b: 0, a: 1 }
```

The conversion fails for standard `rgb()` strings. Only `rgba()` format seems to be working now.

### Expected behavior

Both `rgb()` and `rgba()` color formats should be properly converted to RGBA objects. The function should handle:
- `rgb(255, 0, 0)` → `{ r: 255, g: 0, b: 0, a: 1 }`
- `rgba(255, 0, 0, 0.5)` → `{ r: 255, g: 0, b: 0, a: 0.5 }`

### System Info
- @mantine/core version: latest
- Browser: Chrome

This started happening recently, possibly after a recent update. The `rgb()` format used to work fine before.

---
Repository: /testbed
