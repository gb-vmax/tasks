# Bug Report

### Describe the bug

The `isElement` utility function is incorrectly identifying non-React elements as valid React elements. This causes issues when trying to validate whether a value is a proper React element before rendering or processing it.

### Reproduction

```jsx
import { isElement } from '@mantine/core';

// These should return false but are returning true
console.log(isElement(null)); // Expected: false, Actual: true
console.log(isElement([])); // Expected: false, Actual: true
console.log(isElement([1, 2, 3])); // Expected: false, Actual: true

// Plain objects without $$typeof should also return false
const plainObject = { foo: 'bar' };
console.log(isElement(plainObject)); // Expected: false, Actual: true
```

### Expected behavior

The function should only return `true` for actual React elements (objects with the proper `$$typeof` symbol). It should return `false` for:
- `null` values
- Arrays (even empty ones)
- Plain JavaScript objects that aren't React elements

This is causing components that rely on `isElement` to incorrectly process non-element values, leading to unexpected rendering behavior.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
