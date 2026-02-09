# Bug Report

### Describe the bug

Logical expressions (`&&` and `||`) are not being optimized correctly in certain scenarios. The bundler seems to be mishandling the evaluation of logical operators, which can lead to incorrect code optimization or tree-shaking behavior.

### Reproduction

```js
// Example 1: OR operator with falsy value
const result1 = false || someFunction();
// Expected: someFunction() should be called
// Actual: incorrect optimization behavior

// Example 2: AND operator with truthy value  
const result2 = true && anotherFunction();
// Expected: anotherFunction() should be called
// Actual: incorrect optimization behavior
```

When using logical expressions in my code, the bundler appears to be making incorrect assumptions about which branch will be executed. This affects dead code elimination and can result in unexpected runtime behavior.

### Expected behavior

Logical operators should be evaluated correctly:
- For `||` operator: if left side is falsy, right side should be evaluated
- For `&&` operator: if left side is truthy, right side should be evaluated

The bundler should properly optimize these expressions without breaking the intended logic.

### Additional context

This seems to affect code that relies on short-circuit evaluation patterns, particularly when combined with function calls or complex expressions on the right-hand side of the logical operator.

---
Repository: /testbed
