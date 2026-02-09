# Bug Report

### Describe the bug

I'm encountering unexpected behavior when calling functions returned from object properties. The function calls are being treated as having side effects even when they should be pure, which is affecting tree-shaking and optimization.

### Reproduction

```js
const obj = {
  method() {
    return () => 42;
  }
};

// Call the returned function
const fn = obj.method();
const result = fn();
```

When this pattern is used, the bundler incorrectly analyzes the purity of the function call. It seems like the return expression analysis is not working as expected for nested function calls.

### Expected behavior

Function calls should be correctly identified as pure when they don't have side effects, allowing proper tree-shaking and dead code elimination.

### Additional context

This appears to be related to how the bundler tracks return expressions when analyzing call paths. The issue manifests in production builds where code that should be eliminated is still included in the bundle.

---
Repository: /testbed
