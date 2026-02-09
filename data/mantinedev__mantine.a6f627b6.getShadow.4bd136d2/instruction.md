# Bug Report

### Describe the bug

The `getShadow` utility function is not handling falsy values correctly. When passing `0` or an empty string `''` as a shadow size, the function returns `undefined` instead of processing these as valid shadow values.

### Reproduction

```js
import { getShadow } from '@mantine/core';

// These should return valid shadow values but return undefined
console.log(getShadow(0));        // Returns: undefined (unexpected)
console.log(getShadow(''));       // Returns: undefined (unexpected)

// Only null should return undefined
console.log(getShadow(null));     // Returns: undefined (expected)
```

### Expected behavior

The function should only return `undefined` for `null` values. Other falsy values like `0` or empty strings should be processed as valid shadow size inputs and return the corresponding shadow value from the theme.

### System Info
- @mantine/core version: latest
- Framework: React

---
Repository: /testbed
