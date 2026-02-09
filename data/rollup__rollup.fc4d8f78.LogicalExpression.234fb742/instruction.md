# Bug Report

### Describe the bug

I'm encountering incorrect behavior with logical expressions when using the `||` and `&&` operators. It seems like the operators are being evaluated in reverse - `||` is behaving like `&&` and vice versa.

### Reproduction

```js
// Using || operator
const result1 = false || getValue();
// Expected: getValue() should be called and returned
// Actual: Returns false instead

// Using && operator  
const result2 = true && getValue();
// Expected: getValue() should be called and returned
// Actual: Returns true instead
```

The issue appears to be related to how the literal values are being evaluated during tree-shaking or optimization passes. When the right side of a logical expression should be used based on the operator and left value, the wrong branch seems to be selected.

### Expected behavior

- `||` operator should return the right operand when the left is falsy
- `&&` operator should return the right operand when the left is truthy
- `??` operator should return the right operand when the left is null or undefined

### Additional context

This seems to have broken after a recent change. The operators are working backwards from their expected behavior, which is causing incorrect code optimization and potentially removing code that should be included in the bundle.

---
Repository: /testbed
