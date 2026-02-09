# Bug Report

### Describe the bug

The `rem()` converter function is not handling the string value `'0'` correctly. When passing `'0'` as a string, it's being returned as-is instead of being converted to `'0rem'` (or the appropriate unit).

### Reproduction

```js
import { rem } from '@mantine/core';

// This should return '0rem' but returns '0'
console.log(rem('0')); // Expected: '0rem', Actual: '0'

// Numeric 0 works correctly
console.log(rem(0)); // Returns: '0rem' ✓
```

The issue appears when using string `'0'` values, which might come from props or other string-based inputs. The converter treats numeric `0` and string `'0'` differently, leading to inconsistent behavior.

### Expected behavior

Both `rem(0)` and `rem('0')` should return `'0rem'` for consistency. String representations of zero should be handled the same way as numeric zero.

### System Info
- @mantine/core version: latest
- Framework: React

---
Repository: /testbed
