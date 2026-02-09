# Bug Report

### Describe the bug

When using sequence expressions with a single element, the output is incorrectly formatted with an extra comma. The generated code shows `(, element)` instead of the expected `(element)`.

### Reproduction

```js
// Input: sequence expression with one element
const ast = {
  type: 'SequenceExpression',
  expressions: [
    { type: 'Identifier', name: 'x' }
  ]
};

// Generated output: (, x)
// Expected output: (x)
```

This appears to affect any sequence expression containing only a single node. When there are multiple elements, the formatting works correctly, but single-element sequences produce invalid syntax with a leading comma.

### Expected behavior

A sequence expression with a single element should be formatted as `(element)` without any commas. The comma separator should only appear between multiple elements.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
