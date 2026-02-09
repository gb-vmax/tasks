# Bug Report

### Describe the bug

When using shorthand hex colors (3-character format like `#abc`), the color conversion is producing incorrect RGB values. The red and green channels appear to be swapped or incorrectly calculated.

### Reproduction

```js
import { toRgba } from '@mantine/core';

// Using a shorthand hex color
const result = toRgba('#f0a');
console.log(result);
// Expected: { r: 255, g: 0, b: 170, a: 1 }
// Actual: incorrect RGB values with swapped channels
```

### Expected behavior

Shorthand hex colors should be properly expanded and converted to the correct RGBA values. For example:
- `#f0a` should expand to `#ff00aa` and convert to `{ r: 255, g: 0, b: 170, a: 1 }`
- `#abc` should expand to `#aabbcc` and convert to `{ r: 170, g: 187, b: 204, a: 1 }`

### System Info
- @mantine/core version: latest
- Browser: Chrome

---
Repository: /testbed
