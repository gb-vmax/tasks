# Bug Report

### Describe the bug

I'm encountering an issue where function parameters with the same identifier variable are being incorrectly marked as reassigned, causing unexpected deoptimization behavior. When calling a function multiple times with the same identifier argument, the parameter optimization is lost after the first call.

### Reproduction

```js
function processValue(param) {
  // Some operation using param
  return param.someProperty;
}

const myVar = createIdentifier();

// First call works as expected
processValue(myVar);

// Second call with the same identifier triggers incorrect reassignment detection
processValue(myVar);
```

The parameter variable tracking seems to be treating identical identifier variables as different values, which causes the known value optimization to be cleared when it shouldn't be.

### Expected behavior

When a function is called multiple times with the same identifier variable as an argument, the parameter should maintain its known value optimization. The parameter should only be marked as reassigned when actually called with a *different* argument.

### Additional context

This appears to affect tree-shaking and dead code elimination in cases where functions are called repeatedly with the same variable reference. The optimization that should be preserved across multiple calls with identical arguments is being lost.

---
Repository: /testbed
