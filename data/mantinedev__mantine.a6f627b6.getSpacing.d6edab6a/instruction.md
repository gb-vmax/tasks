# Bug Report

### Describe the bug

The `getSpacing` utility function is not working correctly - it's wrapping the size value in an object with a `value` property before passing it to `getSize`, which breaks the expected behavior. When I try to use spacing values, they're not being processed properly.

### Reproduction

```js
import { getSpacing } from '@mantine/core';

// This should return the correct spacing value
const spacing = getSpacing('md');
console.log(spacing); // Returns unexpected result

// Same issue with numeric values
const numericSpacing = getSpacing(16);
console.log(numericSpacing); // Also not working as expected
```

### Expected behavior

`getSpacing` should accept a size value (string or number) and return the corresponding spacing CSS variable or rem value, just like how `getSize` and `getRadius` work. It should handle the value directly without wrapping it in an object.

### System Info
- @mantine/core version: latest
- Browser: Chrome

---
Repository: /testbed
