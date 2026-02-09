# Bug Report

### Describe the bug

I'm experiencing an issue with function parameter handling when the `arguments` object is used. It seems like function parameters are not being included correctly in certain scenarios involving the `arguments` variable.

### Reproduction

```js
function test() {
  // When arguments is NOT used, parameters should be included
  const x = arguments; // arguments is accessed
  return function(a, b, c) {
    // These parameters should be handled differently
    // depending on whether arguments is used in the scope
    return a + b + c;
  }
}
```

The issue appears when:
1. A function has parameters that are simple identifiers
2. The `arguments` variable is involved in the scope
3. The inclusion logic determines which parameters should be processed

### Expected behavior

Function parameters should be included in the output based on whether they're identifiers and whether the `arguments` object is being used in that scope. The current behavior seems inverted - parameters are being included when they shouldn't be and vice versa.

### Additional context

This is affecting tree-shaking and code inclusion logic. Functions with unused parameters aren't being optimized correctly when `arguments` is present.

---
Repository: /testbed
