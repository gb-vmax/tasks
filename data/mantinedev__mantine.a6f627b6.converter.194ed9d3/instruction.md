# Bug Report

### Describe the bug

When using the `rem()` converter utility with the string value `'0'`, it's not being converted properly. The function should treat the string `'0'` the same way as the number `0` and return `'0rem'`, but instead it's being processed as a regular string and going through the pixel conversion logic.

### Reproduction

```js
import { rem } from '@mantine/core';

// This works correctly
console.log(rem(0)); // Expected: '0rem'

// This doesn't work as expected
console.log(rem('0')); // Expected: '0rem', but gets incorrect conversion
```

The issue occurs when passing `'0'` as a string instead of a number. The converter should handle both cases identically since they represent the same value.

### Expected behavior

Both `rem(0)` and `rem('0')` should return `'0rem'` consistently.

### System Info

- @mantine/core version: latest
- Browser: All browsers affected

---
Repository: /testbed
