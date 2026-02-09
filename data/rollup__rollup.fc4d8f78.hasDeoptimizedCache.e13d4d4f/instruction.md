# Bug Report

### Describe the bug

I'm experiencing an issue with logical expressions where the deoptimization cache seems to be inverted. When working with complex logical expressions (like `&&` or `||`), the compiler appears to be caching results incorrectly, leading to unexpected behavior in tree-shaking and dead code elimination.

### Reproduction

```js
// Example code that triggers the issue
const result = condition1 && condition2 || condition3;

// The deoptimization cache gets set with inverted values
// causing incorrect optimization decisions
```

When the deoptimization cache is updated for logical expressions, it seems to store the opposite of what it should. This causes the compiler to make wrong assumptions about whether certain code paths can be eliminated or not.

### Expected behavior

The deoptimization cache should correctly reflect whether a logical expression has been deoptimized. When setting the cache flag to `true`, it should be stored as `true`, not inverted to `false`.

### System Info
- Rollup version: latest
- Node version: 18.x

This appears to affect any code using logical operators where the compiler needs to track deoptimization state. The issue manifests as incorrect tree-shaking behavior or unexpected code being included/excluded in the final bundle.

---
Repository: /testbed
