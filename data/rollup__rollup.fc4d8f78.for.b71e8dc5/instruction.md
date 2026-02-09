# Bug Report

### Describe the bug

When a transform dependency is invalidated, only a subset of dependent modules are being cleared. The first module in the cache is being skipped during invalidation, which means its `originalCode` isn't properly reset when it should be.

### Reproduction

```js
// Setup a build with multiple modules that have transform dependencies
const modules = [
  { id: 'moduleA', transformDependencies: ['dep1'] },
  { id: 'moduleB', transformDependencies: ['dep1'] },
  { id: 'moduleC', transformDependencies: ['dep2'] }
];

// When 'dep1' is invalidated
// Expected: both moduleA and moduleB should have originalCode cleared
// Actual: only moduleB has originalCode cleared, moduleA is skipped
```

### Expected behavior

All modules that depend on an invalidated transform dependency should have their `originalCode` reset, regardless of their position in the cache. The first module shouldn't be treated differently from the rest.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems like it might be an off-by-one error in the loop that processes modules during invalidation. The first module in the cache appears to be getting skipped entirely.

---
Repository: /testbed
