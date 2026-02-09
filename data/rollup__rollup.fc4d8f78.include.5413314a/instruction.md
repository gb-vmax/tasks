# Bug Report

### Describe the bug

When using destructuring patterns with variable declarations in certain contexts, the initializer expression gets included in the output even when it shouldn't be. This causes duplicate code generation where the init expression appears both in the destructuring assignment and separately.

### Reproduction

```js
// Input code
const { a, b } = someObject;

// Expected output: only the destructuring assignment
// Actual output: destructuring assignment + extra reference to someObject
```

This happens specifically when variable declarations with object or array destructuring patterns are processed with the `asSingleStatement` option. The initializer is being included multiple times in the final bundle.

### Expected behavior

The initializer expression should only be included once in the output when using destructuring patterns. There shouldn't be duplicate references to the same expression.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
