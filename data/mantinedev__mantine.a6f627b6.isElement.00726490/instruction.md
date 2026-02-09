# Bug Report

### Describe the bug

The `isElement` utility function is incorrectly identifying React Fragments as valid elements, which is causing unexpected behavior in components that rely on element type checking.

### Reproduction

```jsx
import { Fragment } from 'react';
import { isElement } from '@mantine/core';

// This now returns true, but Fragments should not be treated as regular elements
const result = isElement(<Fragment><div>test</div></Fragment>);
console.log(result); // true (unexpected)

// Expected: false
// Actual: true
```

### Expected behavior

React Fragments should not be identified as regular React elements by the `isElement` function. Fragments are special constructs and should be filtered out, similar to how arrays and null values are handled.

This is causing issues in components that need to differentiate between actual renderable elements and Fragment wrappers.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
