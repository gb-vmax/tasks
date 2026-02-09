# Bug Report

### Describe the bug

When using short hex color codes (3 characters) with the `toRgba` function, the colors are being converted incorrectly. The RGB values don't match what they should be for the given hex input.

### Reproduction

```js
import { toRgba } from '@mantine/core';

// Using a short hex code like #f00 (red)
const result = toRgba('#f00');
console.log(result);
// Expected: { r: 255, g: 0, b: 0, a: 1 }
// Actual: incorrect RGB values
```

The conversion seems to be mapping the hex digits to the wrong RGB channels. For example, `#f00` should expand to `#ff0000` (full red, no green, no blue), but the actual output doesn't match this.

### Expected behavior

Short hex codes should be properly expanded to their 6-character equivalents before conversion:
- `#f00` → `#ff0000` → `{ r: 255, g: 0, b: 0, a: 1 }`
- `#0f0` → `#00ff00` → `{ r: 0, g: 255, b: 0, a: 1 }`
- `#00f` → `#0000ff` → `{ r: 0, g: 0, b: 255, a: 1 }`

### System Info

- @mantine/core version: latest
- Browser: All browsers affected

---
Repository: /testbed
