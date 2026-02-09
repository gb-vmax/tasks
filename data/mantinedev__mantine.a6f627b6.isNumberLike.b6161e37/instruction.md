# Bug Report

### Describe the bug

The `isNumberLike` utility function is not correctly identifying CSS function values like `calc()` and `var()`. When passing strings that start with these CSS functions, they are being rejected as invalid number-like values even though they should be accepted.

### Reproduction

```js
import { isNumberLike } from '@mantine/core';

// These should return true but are returning false
console.log(isNumberLike('calc(100% - 20px)')); // Expected: true, Actual: false
console.log(isNumberLike('var(--my-variable)')); // Expected: true, Actual: false
console.log(isNumberLike('calc(50vh + 10px)')); // Expected: true, Actual: false
```

### Expected behavior

CSS function values like `calc()` and `var()` should be recognized as valid number-like values since they are commonly used in CSS properties that accept numeric values.

### System Info
- @mantine/core version: latest
- Browser: Chrome 120

---
Repository: /testbed
