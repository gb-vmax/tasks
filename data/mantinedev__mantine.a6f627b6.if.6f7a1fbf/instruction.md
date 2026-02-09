# Bug Report

### Describe the bug

When using `getBaseValue()` with object-based style props, the function is not correctly extracting the `base` value. Instead, it appears to be returning the entire value unchanged in cases where an object with a `base` property is passed.

### Reproduction

```js
import { getBaseValue } from '@mantine/core';

// This should return 'sm' but returns undefined
const result1 = getBaseValue({ base: 'sm', xs: 'md' });
console.log(result1); // Expected: 'sm', Actual: undefined

// This should return the base value
const result2 = getBaseValue({ base: 10, sm: 20 });
console.log(result2); // Expected: 10, Actual: undefined

// Non-object values work fine
const result3 = getBaseValue('lg');
console.log(result3); // Works correctly: 'lg'
```

### Expected behavior

When passing an object with a `base` property to `getBaseValue()`, it should return the value of the `base` property. For non-object values, it should return the value as-is.

### System Info
- @mantine/core version: latest
- Framework: React

---
Repository: /testbed
