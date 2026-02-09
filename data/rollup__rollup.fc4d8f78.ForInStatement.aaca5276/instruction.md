# Bug Report

### Describe the bug

I'm experiencing an issue with tree-shaking in for-in loops where code that should be removed is being incorrectly retained in the bundle. It seems like the loop variable assignment is always being included even when `includeChildrenRecursively` is `false`.

### Reproduction

```js
// Input code
for (const key in obj) {
  // Empty loop body or side-effect-free operations
}
```

When bundling code with for-in statements, the left-hand side (loop variable) is being included in cases where it shouldn't be. This causes unnecessary code to appear in the final bundle.

### Expected behavior

When `includeChildrenRecursively` is `false`, the loop variable assignment should only be included if necessary. The bundler should properly tree-shake for-in loops based on whether they have actual side effects.

### Additional context

This appears to be affecting the tree-shaking optimization pass. The loop variable is being treated as if it always needs to be included, even in scenarios where the loop could potentially be removed entirely.

---
Repository: /testbed
