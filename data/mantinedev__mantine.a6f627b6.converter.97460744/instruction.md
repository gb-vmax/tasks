# Bug Report

### Describe the bug

The `rem()` utility function is converting pixel values incorrectly. Instead of dividing by 16 to convert px to rem, it appears to be multiplying by 16, resulting in values that are 256 times larger than expected.

### Reproduction

```js
import { rem } from '@mantine/core';

// Expected: "1rem" (16px / 16 = 1rem)
// Actual: "256rem" (16px * 16 = 256rem)
console.log(rem(16)); 

// Expected: "2rem" (32px / 16 = 2rem)
// Actual: "512rem" (32px * 16 = 512rem)
console.log(rem(32));

// String values with 'px' suffix also affected
// Expected: "1.5rem" (24px / 16 = 1.5rem)
// Actual: Incorrect conversion
console.log(rem('24px'));
```

### Expected behavior

The `rem()` function should convert pixel values to rem units by dividing by 16 (the standard browser font size). For example:
- `rem(16)` should return `"1rem"`
- `rem(32)` should return `"2rem"`
- `rem('24px')` should return `"1.5rem"`

### System Info

- @mantine/core version: latest
- Browser: Chrome

This is causing layout issues where elements are appearing much larger than intended when using the rem converter utility.

---
Repository: /testbed
