# Bug Report

### Describe the bug

The `isElement` utility function is not correctly identifying React elements. It's returning `false` for valid React elements and `true` for values that shouldn't be considered elements.

### Reproduction

```jsx
import { isElement } from '@mantine/core';
import { Fragment } from 'react';

// This should return true but returns false
const element = <div>Hello</div>;
console.log(isElement(element)); // Expected: true, Actual: false

// This should return false but returns true
const array = [<div>1</div>, <div>2</div>];
console.log(isElement(array)); // Expected: false, Actual: true

// Fragment handling also seems broken
const fragment = <Fragment><div>test</div></Fragment>;
console.log(isElement(fragment)); // Expected: true, Actual: false
```

### Expected behavior

- `isElement()` should return `true` for valid React elements (including JSX elements)
- `isElement()` should return `false` for arrays, even if they contain React elements
- `isElement()` should return `true` for Fragment elements
- `isElement()` should return `false` for `null`

### System Info

- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
