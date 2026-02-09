# Bug Report

### Describe the bug

The `getSingleElementChild` utility function is returning unexpected results. When passing a single valid React element as a child, the function returns `null` instead of the element itself. Additionally, when passing multiple children, it seems to be returning the last child instead of `null`.

### Reproduction

```jsx
import { getSingleElementChild } from '@mantine/core';

// Case 1: Single element child - returns null (unexpected)
const singleChild = <div>Test</div>;
const result1 = getSingleElementChild(singleChild);
console.log(result1); // Expected: <div>Test</div>, Got: null

// Case 2: Multiple children - returns last child (unexpected)
const multipleChildren = (
  <>
    <div>First</div>
    <div>Second</div>
  </>
);
const result2 = getSingleElementChild(multipleChildren);
console.log(result2); // Expected: null, Got: <div>Second</div>
```

### Expected behavior

The function should:
- Return the child element when exactly one React element is passed
- Return `null` when zero children or multiple children are passed
- Return `null` when the child is not a valid React element

### System Info
- @mantine/core version: latest
- React version: 18.x

This is breaking components that rely on this utility to validate single-child requirements.

---
Repository: /testbed
