# Bug Report

### Describe the bug

I'm experiencing an issue where certain markdown parsing operations are not working correctly. It seems like some validation logic is broken - things that should be allowed are being rejected, and the parser is skipping elements that should be processed.

### Reproduction

```js
// When checking if certain markdown elements are in scope
// with a single-element list, the function incorrectly returns 
// the fallback value instead of checking the list

const stack = ['paragraph', 'list', 'blockquote'];
const toCheck = ['list'];

// This should return true since 'list' is in the stack
// but instead returns the fallback value
```

The issue appears when validating whether specific markdown constructs are allowed in the current parsing context. When passing a single element to check, it's being treated as if no elements were provided.

### Expected behavior

When checking if a single markdown element type is in the current scope/stack, it should properly iterate through and check that element. The function should only return the fallback value when the list is actually empty (length 0), not when it contains exactly 1 element.

### System Info
- remark version: 15.0.1
- Browser: N/A (Node.js environment)

---
Repository: /testbed
