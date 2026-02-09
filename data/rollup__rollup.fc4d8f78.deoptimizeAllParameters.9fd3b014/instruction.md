# Bug Report

### Describe the bug

I'm experiencing an issue with function parameter handling where the first parameter appears to be skipped during deoptimization. This is causing incorrect behavior when analyzing function parameters in certain scenarios.

### Reproduction

```js
function example(a, b, c) {
  // When deoptimization occurs, parameter 'a' is not being processed
  // Only parameters b and c are deoptimized
  return a + b + c;
}
```

The deoptimization logic seems to be starting from index 1 instead of 0, which means the first parameter is never deoptimized. Additionally, there's some weird behavior where only the first variable in each parameter is being marked as reassigned due to an early break statement.

### Expected behavior

All parameters (including the first one) should be deoptimized and marked as reassigned when `deoptimizeAllParameters()` is called. The current implementation skips the first parameter entirely and doesn't properly mark all variables as reassigned.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
