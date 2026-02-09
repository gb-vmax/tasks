# Bug Report

### Describe the bug

I'm encountering an issue with return value handling in functions. When a function has exactly one return statement, the return value scope seems to be incorrectly initialized or not tracked at all.

### Reproduction

```js
function singleReturn() {
  return 42;
}

const result = singleReturn();
// Expected: result should be properly analyzed
// Actual: return value tracking appears broken
```

The issue appears to affect functions with a single return statement. Functions with multiple returns or no returns seem to work differently.

### Expected behavior

Functions with one return statement should have their return values properly tracked and analyzed. The return expression should be accessible and correctly represent the actual return value.

### Additional context

This seems related to how return expressions are being collected and processed. The behavior changed recently and is causing issues with type inference and optimization passes that rely on understanding what a function returns.

---
Repository: /testbed
