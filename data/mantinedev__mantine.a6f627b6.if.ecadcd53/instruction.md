# Bug Report

### Describe the bug

When using responsive style props with object notation but without a `base` property defined, the function returns `null` instead of `undefined`. This breaks the expected behavior where omitting the `base` property should fall through to use default values.

### Reproduction

```js
import { getBaseValue } from '@mantine/core';

// Case 1: Object with other breakpoint values but no base
const styleValue = {
  xs: '10px',
  md: '20px'
  // no base property
};

const result = getBaseValue(styleValue);
console.log(result); // Returns: null
// Expected: undefined
```

### Expected behavior

When a responsive style object doesn't include a `base` property, `getBaseValue()` should return `undefined` to allow fallback to default values. Currently it returns `null` which prevents proper fallback behavior.

### System Info
- @mantine/core version: latest
- Framework: React

---
Repository: /testbed
