# Bug Report

### Describe the bug

Sequence expressions are not being evaluated correctly for side effects. When a sequence expression contains multiple expressions, the last expression's side effects are being ignored during the tree-shaking analysis.

### Reproduction

```js
// Input code
const result = (sideEffect1(), sideEffect2(), returnValue);

// Expected: Both sideEffect1() and sideEffect2() should be preserved
// Actual: sideEffect2() is being removed during tree-shaking
```

This affects code like:
```js
export const value = (console.log('init'), doSetup(), 42);
```

The final expression in the sequence is being treated as if it has no side effects, causing incorrect tree-shaking behavior where important function calls are removed from the output.

### Expected behavior

All expressions in a sequence should be checked for side effects, including the last one. The tree-shaker should preserve expressions that have side effects regardless of their position in the sequence.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
