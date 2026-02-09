# Bug Report

### Describe the bug

The `getShadow` utility function is not returning shadow values correctly. When I pass a valid shadow size, it returns `undefined` instead of the expected shadow CSS variable.

### Reproduction

```js
import { getShadow } from '@mantine/core';

// This returns undefined when it should return the shadow value
const shadow = getShadow('sm');
console.log(shadow); // undefined

// Even with explicit shadow sizes
const largeShadow = getShadow('lg');
console.log(largeShadow); // undefined
```

### Expected behavior

The function should return the appropriate shadow CSS variable (e.g., `var(--mantine-shadow-sm)`) when a valid shadow size is provided. It should only return `undefined` when no size is passed or the size is falsy.

### System Info
- @mantine/core version: latest
- Browser: Chrome

---
Repository: /testbed
