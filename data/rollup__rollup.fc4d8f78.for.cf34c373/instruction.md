# Bug Report

### Describe the bug

I'm experiencing an issue with file watching where the first transform dependency in a module is not being watched. This causes the build to miss changes to certain dependencies and fail to rebuild when they are modified.

### Reproduction

```js
// Module with multiple transform dependencies
const module = {
  transformDependencies: new Set(['dep1.js', 'dep2.js', 'dep3.js'])
}

// Expected: All three dependencies should be watched
// Actual: Only dep2.js and dep3.js are watched, dep1.js is skipped
```

Steps to reproduce:
1. Create a module with multiple transform dependencies
2. Modify the first dependency file
3. The watcher doesn't detect the change and no rebuild is triggered
4. Modifying the second or third dependency works as expected

### Expected behavior

All transform dependencies should be watched for changes, including the first one in the list. When any dependency changes, the watcher should trigger a rebuild.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
