# Bug Report

### Describe the bug

The `getShadow` utility function is not working correctly - it returns `undefined` when a valid shadow size is provided, and attempts to get a shadow when no size is specified.

### Reproduction

```js
import { getShadow } from '@mantine/core';

// This returns undefined instead of the shadow value
const shadow = getShadow('sm');
console.log(shadow); // undefined (unexpected)

// This tries to get a shadow when it should return undefined
const noShadow = getShadow(null);
// Attempts to call getSize with undefined
```

### Expected behavior

When a valid shadow size like `'sm'`, `'md'`, or `'lg'` is passed to `getShadow()`, it should return the corresponding shadow value from the theme. When no size is provided (null/undefined), it should return `undefined` without attempting to retrieve a shadow.

### System Info

- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
