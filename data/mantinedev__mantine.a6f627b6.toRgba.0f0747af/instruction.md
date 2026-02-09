# Bug Report

### Describe the bug

The `toRgba()` function is not properly handling `rgb()` color strings (without alpha channel). When I pass a color like `rgb(255, 0, 0)`, it's not being converted correctly and falls through to return the default black color.

### Reproduction

```js
import { toRgba } from '@mantine/core';

// This doesn't work as expected
const result = toRgba('rgb(255, 0, 0)');
console.log(result); // Expected: { r: 255, g: 0, b: 0, a: 1 }
                     // Actual: { r: 0, g: 0, b: 0, a: 0 }

// Only rgba() format seems to work
const result2 = toRgba('rgba(255, 0, 0, 1)');
console.log(result2); // This works correctly
```

### Expected behavior

The function should handle both `rgb()` and `rgba()` color formats correctly. Currently it only seems to work with `rgba()` strings.

### System Info

- @mantine/core version: latest
- Browser: Chrome 120

---
Repository: /testbed
