# Bug Report

### Describe the bug

I'm experiencing an issue with unit conversion functions where passing the string `'0'` as a value doesn't get converted properly. Instead of returning `'0rem'` (or `'0em'`), it seems to be processing it as a regular value and attempting conversion.

Also, when passing pixel values like `'16px'` or `'32px'`, the converter is not working at all - it's just returning the original value unchanged instead of converting to rem/em units.

### Reproduction

```js
import { rem } from '@mantine/core';

// This doesn't work as expected
console.log(rem('0')); // Should return '0rem' but doesn't

// These also don't convert properly
console.log(rem('16px')); // Should return '1rem' but returns '16px'
console.log(rem('32px')); // Should return '2rem' but returns '32px'
```

### Expected behavior

- `rem('0')` should return `'0rem'`
- `rem('16px')` should return `'1rem'`
- `rem('32px')` should return `'2rem'`

The converter should handle both numeric zero and string `'0'`, and should properly convert pixel values to rem units.

### System Info

- @mantine/core version: latest
- Browser: Chrome 120

---
Repository: /testbed
