# Bug Report

### Describe the bug

The `isElement` utility function is not correctly identifying React elements. It's returning `true` for `null` values and Fragment components, which should not be considered valid elements according to the function's purpose.

### Reproduction

```js
import { isElement } from '@mantine/core';
import { Fragment } from 'react';

// This incorrectly returns true
console.log(isElement(null)); // Expected: false, Actual: true

// This incorrectly returns false
console.log(isElement(<Fragment />)); // Expected: true, Actual: false

// Regular elements work as expected
console.log(isElement(<div />)); // Returns: true
```

### Expected behavior

- `isElement(null)` should return `false` since `null` is not a React element
- `isElement(<Fragment />)` should return `true` since Fragment is a valid React element type
- Regular React elements should continue to return `true`

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
