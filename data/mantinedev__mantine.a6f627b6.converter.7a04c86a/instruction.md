# Bug Report

### Describe the bug

When passing `0` or `'0'` values to the `rem()` converter function, it returns just `'0'` without the unit suffix. This is inconsistent with the expected behavior where unit converters should always include the unit (e.g., `'0rem'`).

### Reproduction

```js
import { rem } from '@mantine/core';

console.log(rem(0));    // Returns: '0' (expected: '0rem')
console.log(rem('0'));  // Returns: '0' (expected: '0rem')
console.log(rem(16));   // Returns: '1rem' (works correctly)
```

### Expected behavior

The converter should return `'0rem'` (or `'0em'` for the `em()` function) when the input value is `0` or `'0'`, maintaining consistency with other return values that include the unit suffix.

### System Info
- @mantine/core version: latest
- This affects styling calculations where the unit is expected to be present

---
Repository: /testbed
