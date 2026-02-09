# Bug Report

### Describe the bug

Functions are returning `UNKNOWN_RETURN_EXPRESSION` when called directly instead of their actual return expression. This is causing incorrect tree-shaking behavior where code that should be preserved is being removed or vice versa.

### Reproduction

```js
// Function that returns a simple value
function getValue() {
  return 42;
}

// When analyzing the return value of getValue()
const result = getValue();

// Expected: Should recognize the return value as the literal 42
// Actual: Treats the return value as unknown
```

This affects any direct function call analysis. The return expression is not being properly evaluated, which impacts dead code elimination and optimization.

### Expected behavior

When a function is called directly (without any property access path), the bundler should analyze and return the actual return expression from the function's scope, not treat it as an unknown value.

### Additional context

This seems to affect both sync and async functions. The issue appears to be in how the call path length is being checked - direct calls should be handled differently than property access on function objects.

---
Repository: /testbed
