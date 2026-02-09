# Bug Report

### Describe the bug

I'm experiencing an issue with logical expressions where deoptimization caching appears to be inverted. When the cache should be marked as deoptimized, it's being set to the opposite state, which causes incorrect optimization behavior in the bundler.

### Reproduction

```js
// Create a logical expression that should trigger deoptimization
const code = `
  const x = foo || bar;
  x.someMethod();
`;

// The deoptimization cache flag gets set incorrectly
// Expected: cache flag should be true when deoptimized
// Actual: cache flag becomes false when it should be true
```

### Expected behavior

When a logical expression is deoptimized, the `hasDeoptimizedCache` flag should be set to `true` to indicate that deoptimization has occurred. Currently, the flag is being set to the inverted value, causing the bundler to incorrectly assume optimization states.

This leads to:
- Incorrect tree-shaking decisions
- Potential runtime errors due to over-aggressive optimizations
- Inconsistent behavior between similar code patterns

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
