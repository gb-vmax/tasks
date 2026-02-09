# Bug Report

### Describe the bug

I'm experiencing an issue with `for...of` loops where the loop body and its contents are being included in the bundle even when they shouldn't be. It seems like the tree-shaking logic isn't working correctly for `for...of` statements.

### Reproduction

```js
// This for...of loop gets included in the bundle even though
// it should be tree-shaken away
for (const item of unusedArray) {
  console.log(item);
}
```

When bundling code that contains `for...of` loops that reference unused variables or have side-effect-free bodies, the entire loop is still being included in the final output. This is causing unnecessary code bloat.

### Expected behavior

The `for...of` loop and its body should be tree-shaken away when:
1. The loop variable is never used elsewhere
2. The iterable is not used
3. The loop body has no side effects

Instead, it appears the loop is always being marked as included in the bundle regardless of whether it's actually needed.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
