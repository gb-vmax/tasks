# Bug Report

### Describe the bug

I'm experiencing an issue with function deoptimization where reassignments to function properties are not being properly tracked. When a function object has an unknown property reassigned, the return expression and parameters should be deoptimized, but this doesn't seem to be happening correctly.

### Reproduction

```js
function myFunction() {
  return someValue;
}

// Reassign an unknown property on the function
myFunction[unknownKey] = newValue;

// The function's return expression and parameters should be deoptimized
// but they remain optimized
```

### Expected behavior

When a function object has properties reassigned (especially with unknown keys), the function should properly deoptimize its return expression and all parameters to account for potential side effects. This is critical for tree-shaking and optimization correctness.

### Additional context

This appears to be related to how the deoptimization path is being checked. The issue manifests when dealing with dynamic property access on function objects, which should trigger a full deoptimization of the function's internals.

---
Repository: /testbed
