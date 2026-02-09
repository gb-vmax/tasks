# Bug Report

### Describe the bug

I'm encountering an issue with tree-shaking/dead code elimination where code that should be removed is being kept in the bundle. It seems like the deoptimization logic for parameter variables is not working correctly at certain path depths.

### Reproduction

When bundling code with nested property access on function parameters (path length of 2), the code is not being properly optimized. The deoptimization appears to be too aggressive and is preventing valid optimizations from occurring.

```js
function example(obj) {
  // Access at depth 2: obj.a.b
  return obj.a.b;
}

// This type of nested access should allow for proper tree-shaking
// but the bundle size suggests it's being over-deoptimized
```

### Expected behavior

The bundler should properly track and optimize nested property accesses on parameter variables. Code that is provably unused should be eliminated from the final bundle.

Previously, this worked correctly and the bundle was smaller. After a recent update, the bundle size increased noticeably for projects with this pattern.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
