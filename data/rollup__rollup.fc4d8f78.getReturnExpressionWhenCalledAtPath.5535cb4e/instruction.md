# Bug Report

### Describe the bug

I'm experiencing an issue with function call purity tracking. When calling a function through a property path, the purity flag is being incorrectly determined based on whether the path exists rather than the actual purity of the return expression.

### Reproduction

```js
// When calling a method through a property path
const obj = {
  method: function() {
    return someValue;
  }
};

// Calling obj.method() or obj.prop.method()
// The purity tracking seems to depend on the path length
// instead of the actual function's purity
```

This affects tree-shaking behavior since functions that should be marked as pure/impure are being evaluated incorrectly based on the call path.

### Expected behavior

The purity flag should be determined by the actual return expression's purity, not by whether a path was provided. Functions should be consistently marked as pure or impure regardless of how they're accessed (direct call vs property access).

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
