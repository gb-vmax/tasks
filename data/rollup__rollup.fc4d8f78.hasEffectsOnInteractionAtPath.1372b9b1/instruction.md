# Bug Report

### Describe the bug

I'm experiencing an issue where boolean literal values are being treated as having side effects when they shouldn't. This is causing incorrect tree-shaking behavior in my build output - code that should be eliminated as dead code is being retained.

### Reproduction

```js
const result = true.toString();
// This simple property access on a boolean literal is incorrectly 
// flagged as having side effects

if (false) {
  console.log("This should be tree-shaken");
}
// The dead code inside this block is not being removed
```

When accessing properties or methods on boolean literals (like `true` or `false`), the bundler is treating these operations as if they have side effects, which prevents proper optimization.

### Expected behavior

Property access on boolean literals should not be considered as having side effects. Methods like `toString()`, `valueOf()`, etc. on boolean primitives are pure operations and should allow the bundler to properly eliminate unreachable code.

The tree-shaking should work correctly and remove dead code branches that are guarded by boolean literals.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
