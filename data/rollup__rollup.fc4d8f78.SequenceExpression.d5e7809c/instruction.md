# Bug Report

### Describe the bug

When using sequence expressions (comma operator), the last expression in the sequence is not being checked for side effects. This causes the bundler to incorrectly tree-shake code that should be preserved.

### Reproduction

```js
// Example code that triggers the issue
const result = (sideEffect1(), sideEffect2(), pureValue);

// The last expression (pureValue) should also be checked for effects
// Currently only the first expressions are being validated
```

In a sequence expression like `(a, b, c)`, all expressions should be evaluated for side effects, but it appears only the expressions before the last one are being checked. This means if the final expression has side effects, they might not be detected during the analysis phase.

### Expected behavior

All expressions in a sequence should be properly analyzed for side effects, including the last one. The bundler should not remove code that has observable side effects regardless of its position in the sequence.

### Additional context

This seems to affect the tree-shaking behavior where expressions with side effects in the final position of a sequence might get incorrectly removed during the build process.

---
Repository: /testbed
