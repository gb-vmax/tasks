# Bug Report

### Describe the bug

I'm experiencing an issue with shorthand hex color conversion. When using 3-character hex colors (like `#abc`), the resulting RGB values are incorrect. It seems like the conversion is not properly expanding the shorthand notation.

### Reproduction

```js
import { toRgba } from '@mantine/core';

// Using shorthand hex color
const result = toRgba('#abc');
console.log(result);
// Expected: { r: 170, g: 187, b: 204, a: 1 }
// Actual: { r: 170, g: 170, b: 170, a: 1 } (or similar incorrect values)
```

The issue appears when converting 3-digit hex colors. For example, `#abc` should expand to `#aabbcc`, but the conversion produces wrong RGB values.

### Expected behavior

Shorthand hex colors should be properly expanded before conversion:
- `#abc` → `#aabbcc` → `rgb(170, 187, 204)`
- `#f0a` → `#ff00aa` → `rgb(255, 0, 170)`

The function should duplicate each character in the shorthand notation to create the full 6-character hex code.

### System Info

- @mantine/core version: latest
- Browser: Chrome/Firefox

---
Repository: /testbed
