# Bug Report

### Describe the bug

I'm experiencing an issue with module invalidation when transform dependencies change. When a transform dependency is invalidated, modules that don't depend on it are getting their `originalCode` cleared, while modules that actually depend on it are being skipped.

### Reproduction

```js
// Setup: Module A has a transform dependency on file X
// Module B and C don't have any transform dependencies

// When file X changes:
// 1. The invalidation logic runs
// 2. Module A (which depends on X) is NOT invalidated
// 3. Modules B and C (which don't depend on X) ARE invalidated
// 4. This causes incorrect rebuilds and stale cache issues
```

### Expected behavior

When a transform dependency is invalidated, only the modules that actually declare that dependency should have their cache cleared. Modules without the dependency should remain untouched.

Currently it seems like the logic is inverted - modules are being invalidated until we find one that HAS the dependency, instead of only invalidating modules that have the dependency.

### System Info
- Rollup version: latest
- Node version: 18.x

This is causing builds to fail with stale transform results and unnecessary rebuilds of unrelated modules.

---
Repository: /testbed
