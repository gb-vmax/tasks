# Bug Report

### Describe the bug

I'm encountering an issue with `for...in` loops where the loop body effects are being checked before the loop is properly deoptimized. This seems to cause incorrect tree-shaking behavior in certain edge cases.

### Reproduction

```js
// Example code that triggers the issue
for (const key in obj) {
  // When the left side has assignment target effects
  // and the right side has effects, the deoptimization
  // doesn't happen in the correct order
  someFunction(key);
}
```

The problem appears to be that when checking `hasEffects()`, the deoptimization is being applied after checking if the left/right sides have effects, rather than before. This means the loop body effects are evaluated with an incorrectly optimized state.

### Expected behavior

The loop should be deoptimized before checking whether the left side has effects as an assignment target or the right side has effects. This ensures that the loop body effects are checked with the correct optimization state.

### Additional context

This appears to affect tree-shaking decisions for `for...in` statements where both the iterator variable assignment and the iterable expression have side effects.

---
Repository: /testbed
