# Bug Report

### Describe the bug

When declaring multiple variables in a single statement, the first variable declaration is being skipped and not included in the output bundle. Only subsequent declarations after the first one are properly processed.

### Reproduction

```js
// Input code
const a = 1, b = 2, c = 3;

// Expected output: all three variables should be included
// Actual output: only b and c are included, a is missing
```

This also affects destructuring patterns:

```js
const { x } = obj, y = 5;
// Only y is included in the output, the destructuring of x is skipped
```

### Expected behavior

All variable declarations in a multi-declaration statement should be included in the bundle, not just those after the first one.

### Additional context

This appears to affect any `const`, `let`, or `var` statement with multiple comma-separated declarations. The first declarator is consistently being omitted from the output.

---
Repository: /testbed
