# Bug Report

### Describe the bug

The `isNumberLike` utility function is incorrectly identifying CSS values that contain `calc()` or `var()` anywhere in the string as number-like, even when these functions appear in the middle or end of the value rather than at the beginning.

### Reproduction

```js
import { isNumberLike } from '@mantine/core';

// These should NOT be considered number-like but currently return true:
isNumberLike('10px calc(100%)'); // returns true (incorrect)
isNumberLike('something var(--value)'); // returns true (incorrect)
isNumberLike('prefix-calc(10px)'); // returns true (incorrect)

// Only these should return true:
isNumberLike('calc(100% - 20px)'); // should return true
isNumberLike('var(--spacing)'); // should return true
```

### Expected behavior

The function should only consider values as number-like when they **start with** `calc(` or `var(`, not when these strings appear anywhere within the value. CSS function calls are only valid at the beginning of a value expression.

Additionally, the regex seems to be missing the optional `?` quantifier for the unit part, which might cause issues with unitless numeric values in certain contexts.

### System Info
- @mantine/core version: latest
- Browser: N/A (utility function)

---
Repository: /testbed
