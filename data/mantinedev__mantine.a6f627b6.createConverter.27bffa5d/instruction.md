# Bug Report

### Describe the bug

The `rem()` converter function is not handling numeric zero values correctly. When I pass `0` (number) to the function, it's not being converted to `0rem` as expected.

### Reproduction

```js
import { rem } from '@mantine/core';

// This doesn't work anymore
const result = rem(0);
console.log(result); // Expected: '0rem', Actual: undefined or incorrect value

// String zero still works
const result2 = rem('0');
console.log(result2); // Works: '0rem'
```

### Expected behavior

Both numeric `0` and string `'0'` should be converted to `'0rem'`. The function should handle the number zero the same way it handles the string zero.

### System Info
- @mantine/core version: latest
- Browser: Chrome

This seems to have broken recently, possibly after a recent update. The numeric zero case was working before.

---
Repository: /testbed
