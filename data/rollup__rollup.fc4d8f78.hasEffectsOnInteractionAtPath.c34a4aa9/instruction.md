# Bug Report

### Describe the bug

I'm experiencing an issue with boolean literal handling in rollup. When accessing properties on boolean literals, the tree-shaking behavior seems incorrect - it's marking safe property accesses as having side effects when they shouldn't.

### Reproduction

```js
const result = true.toString();
// This is being incorrectly flagged as having effects

const value = false.valueOf();
// Same issue here - basic boolean methods are treated as unsafe
```

When bundling code that accesses built-in methods on boolean literals (like `toString()` or `valueOf()`), rollup is not properly optimizing these calls. The code that should be safely tree-shaken is being kept in the bundle.

### Expected behavior

Direct property access on boolean literals should be recognized as side-effect free. Methods like `toString()` and `valueOf()` on boolean primitives don't have side effects and should be optimized accordingly during the bundling process.

### Additional context

This seems to affect basic boolean operations that are commonly used in production code. The bundle size is larger than expected because these safe operations aren't being properly analyzed.

---
Repository: /testbed
