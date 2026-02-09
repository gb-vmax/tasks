# Bug Report

### Describe the bug

I'm experiencing an issue with logical expressions in my code where the deoptimization logic seems to be inverted. After a recent update, I noticed that my build output is incorrect when using logical operators like `&&` and `||` with complex expressions.

The problem appears to be related to how the deoptimization cache is being handled - it seems like the cache check is backwards, causing the deoptimization to skip when it should run and potentially run when it shouldn't.

### Reproduction

```js
// Example code that triggers the issue
const result = condition && complexExpression() || fallback;

// When this gets processed, the logical expression deoptimization
// doesn't work as expected
```

When bundling code with nested logical expressions, the tree-shaking behavior is not working correctly. Expressions that should be deoptimized are being skipped, leading to incorrect optimization decisions.

### Expected behavior

The deoptimization cache should properly track whether an expression has already been deoptimized. When `deoptimizeCache()` is called:
1. It should check if deoptimization has already occurred
2. If not, it should mark the cache as deoptimized and proceed with the deoptimization logic
3. If already deoptimized, it should return early to avoid redundant work

Currently it seems like the logic is inverted - returning early when it hasn't been deoptimized yet, which causes the deoptimization logic to never run.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
