# Bug Report

### Describe the bug

When using sequence expressions (comma operator) in Rollup, the last expression in the sequence is being excluded from the output bundle even when it should be included. This causes the bundled code to behave incorrectly as the final value of the sequence expression is missing.

### Reproduction

```js
// Input code
export const result = (sideEffect1(), sideEffect2(), finalValue);

// After bundling, the last expression is missing
// Expected: all expressions to be included
// Actual: only side effects are included, finalValue is dropped
```

This seems to affect sequence expressions where the final expression should be retained but is being incorrectly filtered out during the tree-shaking process.

### Expected behavior

All expressions in a sequence should be properly included in the output, especially the last expression which represents the actual value of the sequence expression. The bundler should preserve the complete sequence when necessary.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
