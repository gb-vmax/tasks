# Bug Report

### Describe the bug

I'm experiencing an issue where side effects in my code are not being detected properly. It seems like the analysis is incorrectly reporting that certain operations have side effects when they actually don't, or vice versa.

### Reproduction

```js
// Example code that triggers the issue
function example() {
  const a = 1;
  const b = 2;
  const c = 3;
  // Multiple statements that should be analyzed for side effects
  console.log(a);
  return b + c;
}
```

When analyzing code with multiple statements, the side effect detection appears to be inverted - operations without side effects are flagged as having them, while operations that DO have side effects are being missed.

### Expected behavior

The bundler should correctly identify which statements have side effects and which don't. Pure operations should not be flagged as having side effects, and impure operations (like console.log) should be properly detected.

### System Info
- Rollup version: latest
- Node version: 18.x

This is causing issues with tree-shaking as code that should be eliminated is being kept, and vice versa.

---
Repository: /testbed
