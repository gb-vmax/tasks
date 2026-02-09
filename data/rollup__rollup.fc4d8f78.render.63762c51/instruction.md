# Bug Report

### Describe the bug

When using logical expressions (like `||` or `&&`) in code that gets tree-shaken, the output is malformed when one side of the expression is removed. There appears to be an extra character left behind in the generated code.

### Reproduction

```js
// Input code with logical expression
const value = false || someFunction();

// After tree-shaking when left side is removed
// Expected output: someFunction()
// Actual output: |someFunction()
```

The issue occurs when the bundler determines that one side of a logical expression is unused and tries to remove it. Instead of cleanly removing the unused code and operator, an extra operator character remains in the output.

### Expected behavior

When tree-shaking removes one side of a logical expression, the operator should be completely removed along with the unused branch, leaving only the used expression without any leftover characters.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems to affect any logical expression where dead code elimination is applied. The generated bundle contains invalid JavaScript syntax with the stray operator character.

---
Repository: /testbed
