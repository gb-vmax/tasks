# Bug Report

### Describe the bug

The `isNumberLike` utility function is incorrectly identifying certain string values as number-like when they shouldn't be. I'm seeing issues with empty strings and strings containing whitespace being treated as valid number-like values.

### Reproduction

```js
import { isNumberLike } from '@mantine/core';

// This returns true but should return false
console.log(isNumberLike(''));  // Expected: false, Actual: true

// This also returns true incorrectly
console.log(isNumberLike('   '));  // Expected: false, Actual: true

// Mixed valid/invalid values are being accepted
console.log(isNumberLike('10px invalid'));  // Expected: false, Actual: true
```

### Expected behavior

- Empty strings should not be considered number-like
- Strings with only whitespace should not be considered number-like  
- Strings with mixed valid and invalid CSS units should not be considered number-like
- Only strings that are valid CSS numeric values (like '10px', '1.5rem', 'calc(100% - 20px)', etc.) should return true

### System Info

- @mantine/core version: latest
- Browser: Chrome

This is causing issues in components that rely on this utility to validate numeric inputs, as they're accepting invalid values.

---
Repository: /testbed
