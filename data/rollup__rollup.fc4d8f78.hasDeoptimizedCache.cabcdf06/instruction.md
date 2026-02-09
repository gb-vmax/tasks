# Bug Report

### Describe the bug

I'm encountering an issue with logical expressions where the deoptimization cache flag doesn't seem to be getting set correctly. When setting `hasDeoptimizedCache` to `false`, the flag appears to remain set to `true` instead.

### Reproduction

```js
// Create a logical expression node
const logicalExpr = new LogicalExpression(/* ... */);

// Try to set hasDeoptimizedCache to false
logicalExpr.hasDeoptimizedCache = false;

// Expected: flag should be false
// Actual: flag remains true
```

The setter for `hasDeoptimizedCache` seems to be ignoring the actual value passed to it and always sets the flag to `true` first, then applies some conditional logic that doesn't properly respect the intended value.

### Expected behavior

When setting `hasDeoptimizedCache = false`, the flag should be cleared. When setting `hasDeoptimizedCache = true`, the flag should be set. The setter should directly use the provided value instead of always setting it to `true` initially.

### System Info

- Rollup version: latest
- Node version: 18.x

This appears to be a logic error in the setter implementation that's causing the cache flag to behave incorrectly.

---
Repository: /testbed
