# Bug Report

### Describe the bug

I'm experiencing an issue where function parameters with the same identifier variable are being incorrectly marked as reassigned. This causes unexpected behavior in dead code elimination and tree-shaking.

### Reproduction

```js
function example(param) {
  const x = param;
  // ... some code
  return x;
}

// Call the function multiple times with the same variable
const myVar = 'test';
example(myVar);
example(myVar);
```

When the same variable is passed as an argument to a function in multiple calls, the parameter should not be considered reassigned if it's actually the same variable reference. However, it seems like the parameter is being incorrectly flagged as reassigned even when the argument is identical across calls.

### Expected behavior

When a function parameter receives the same identifier variable across multiple invocations, the parameter's known value should remain stable and not be marked as reassigned. This is important for proper constant propagation and optimization.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
