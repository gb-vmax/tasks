# Bug Report

### Describe the bug

I'm experiencing an issue with parameter deoptimization in function scopes. It seems like the first parameter in a function is not being properly deoptimized when it should be, leading to incorrect optimization assumptions.

### Reproduction

```js
function example(firstParam, secondParam, thirdParam) {
  // Modify parameters
  firstParam.someProperty = 'changed';
  secondParam.anotherProperty = 'modified';
  
  return firstParam;
}

// The first parameter doesn't get deoptimized correctly
// This causes issues with tree-shaking and code optimization
```

### Expected behavior

All parameters should be deoptimized when `deoptimizeAllParameters()` is called, including the first one. Currently it appears that only parameters after the first one are being processed.

### Additional context

This affects bundling and tree-shaking behavior, as the optimizer makes incorrect assumptions about parameter usage. The issue manifests when functions have multiple parameters and they're all supposed to be marked as reassigned/deoptimized.

---
Repository: /testbed
