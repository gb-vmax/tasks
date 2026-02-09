# Bug Report

### Describe the bug

I'm experiencing an issue where calling a function directly (not as a method) is being treated as pure when it should be impure. This is causing incorrect tree-shaking behavior where function calls with side effects are being removed during the build process.

### Reproduction

```js
// Example code that demonstrates the issue
function myFunction() {
  console.log('side effect');
  return 42;
}

// Direct function call
const result = myFunction();

// The function call gets optimized away even though it has side effects
```

When the function is called directly (path length = 0), the bundler incorrectly assumes the call is pure and may remove it during dead code elimination, even though the function has side effects like logging to console.

### Expected behavior

Direct function calls should be treated as potentially impure unless explicitly marked otherwise. The bundler should preserve function calls that might have side effects.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems to have started happening recently. The behavior was working correctly before where function calls were being preserved.

---
Repository: /testbed
