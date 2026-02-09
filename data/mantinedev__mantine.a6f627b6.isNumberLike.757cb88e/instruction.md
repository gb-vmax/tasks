# Bug Report

### Describe the bug

The `isNumberLike` utility function is not correctly validating CSS values with multiple space-separated components. It's accepting values that should be rejected and rejecting values that should be accepted.

### Reproduction

```js
import { isNumberLike } from '@mantine/core';

// This should return false but returns true
console.log(isNumberLike('10px invalid 20px')); // Expected: false, Got: true

// This should return true but returns false  
console.log(isNumberLike('10px 20px 30px')); // Expected: true, Got: false

// Edge case with whitespace-only strings
console.log(isNumberLike('   ')); // Expected: false, Got: true
```

The function seems to have inverted logic when checking space-separated values. Valid multi-value CSS properties (like `margin: 10px 20px 30px`) are being rejected, while strings containing invalid units mixed with valid ones are being accepted.

### Expected behavior

- Strings with only whitespace should return `false`
- Valid space-separated CSS values (e.g., `'10px 20px'`) should return `true`
- Strings containing any invalid CSS values should return `false`

### System Info
- @mantine/core version: latest
- Browser: N/A (utility function)

---
Repository: /testbed
