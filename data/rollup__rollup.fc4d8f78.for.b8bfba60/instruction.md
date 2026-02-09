# Bug Report

### Describe the bug

I've noticed that file watching isn't working properly for transform dependencies. It seems like the first dependency in the list is being skipped and not getting watched, which causes the build to not rebuild when that file changes.

### Reproduction

```js
// Setup a module with multiple transform dependencies
const module = {
  transformDependencies: new Set(['dep1.js', 'dep2.js', 'dep3.js'])
}

// After the watch setup, only dep2.js and dep3.js are being watched
// dep1.js changes don't trigger a rebuild
```

### Expected behavior

All transform dependencies should be watched, including the first one in the set. When any of these dependencies change, the build should be triggered to rebuild.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
