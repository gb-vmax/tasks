# Bug Report

### Describe the bug

When generating code snippets for immediately invoked function expressions (IIFEs), the wrapping logic doesn't work correctly. The generated code has incorrect parentheses placement, which causes syntax errors when the IIFE needs to be wrapped.

### Reproduction

```js
// When generating an IIFE that requires wrapping
// The output has misplaced parentheses

const snippet = getDirectReturnIifeLeft(
  ['x', 'y'],
  'x + y',
  { needsArrowReturnParens: false, needsWrappedFunction: true }
);

// Expected: ((x, y) => x + y)(
// Actual: (x, y) => x + y(
```

The wrapping condition seems to be evaluating incorrectly, leading to malformed IIFE syntax that won't execute properly.

### Expected behavior

IIFEs should be properly wrapped with parentheses when `needsWrappedFunction` is true, regardless of whether arrow functions are being used. The current behavior only wraps when both conditions are met, but standard function expressions also need wrapping when used as IIFEs.

### System Info
- Version: Latest from main branch
- Node: 18.x

---
Repository: /testbed
