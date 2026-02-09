# Bug Report

### Describe the bug

The `getSingleElementChild` utility function is now returning non-element children (like text nodes, fragments, or other React nodes) when it should only return valid React elements. This is causing issues when the function is used in components that expect a single element child.

### Reproduction

```jsx
import { getSingleElementChild } from '@mantine/core';

// Case 1: Multiple children - should return null but returns first child
const result1 = getSingleElementChild(
  <>
    <div>First</div>
    <div>Second</div>
  </>
);
console.log(result1); // Returns <div>First</div> instead of null

// Case 2: Text node - should return null but returns the text
const result2 = getSingleElementChild('Just text');
console.log(result2); // Returns 'Just text' instead of null

// Case 3: Fragment with non-element - should return null but returns the node
const result3 = getSingleElementChild(
  <>
    Some text content
  </>
);
console.log(result3); // Returns text node instead of null
```

### Expected behavior

The function should:
1. Return `null` when there are multiple children
2. Return `null` when the single child is not a valid React element (e.g., text nodes, numbers, etc.)
3. Only return the child when there is exactly one child AND it's a valid React element

This was working correctly before and components relying on this function now receive unexpected node types.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
