# Bug Report

### Describe the bug

I'm experiencing an issue with tree-shaking optimization where certain object properties are not being properly deoptimized during the analysis phase. This appears to be causing incorrect code elimination in some edge cases.

When a parameter variable has nested property access patterns, the deoptimization tracking seems to get out of sync. Specifically, when the same property path is accessed multiple times with different deoptimization contexts, the second access doesn't trigger the necessary deoptimization propagation to dependent entities.

### Reproduction

```js
function test(obj) {
  const x = obj.foo;
  obj.foo.bar = 1;
  const y = obj.foo;
  return x + y;
}
```

In this case, the property `foo` should be marked as deoptimized and propagated to all argument entities that depend on it. However, it seems like the deoptimization is being added to the tracking set before the propagation happens, causing subsequent accesses to be skipped incorrectly.

### Expected behavior

All dependent entities should receive deoptimization notifications for property paths, even when the same path is encountered multiple times during analysis. The deoptimization should propagate to argument entities before being marked as already processed.

### System Info
- Rollup version: latest main branch
- Node version: 18.x

This might be related to the order of operations in the deoptimization tracking logic. The field is being marked as deoptimized before notifying dependent entities, which could cause issues with recursive or repeated property access patterns.

---
Repository: /testbed
