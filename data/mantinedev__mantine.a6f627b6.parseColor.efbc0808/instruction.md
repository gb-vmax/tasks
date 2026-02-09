# Bug Report

### Describe the bug

The `parseColor` function is not correctly handling hex color values anymore. When I pass a hex color string like `#FF5733`, it returns a completely black transparent color instead of parsing the hex value properly.

### Reproduction

```js
import { parseColor } from '@mantine/core';

// This returns { h: 0, s: 0, v: 0, a: 0 } instead of the correct color
const result = parseColor('#FF5733');
console.log(result);

// Expected: A valid HSVA color object representing #FF5733
// Actual: { h: 0, s: 0, v: 0, a: 0 }
```

### Expected behavior

The function should parse hex color strings correctly and return the corresponding HSVA color values. Instead, it's returning a black transparent color (all zeros) for valid hex inputs.

This seems to have broken recently - hex colors were working fine before. Other color formats like `rgb()` or `hsl()` might also be affected.

### System Info
- @mantine/core version: latest
- Browser: Chrome 120

---
Repository: /testbed
