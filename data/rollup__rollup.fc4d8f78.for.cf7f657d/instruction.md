# Bug Report

### Describe the bug

I'm experiencing an issue with file watching where the first transform dependency is not being watched. When a module has transform dependencies, only dependencies after the first one trigger rebuilds when changed.

### Reproduction

```js
// Module with multiple transform dependencies
const module = {
  transformDependencies: new Set([
    'dependency-1.js',
    'dependency-2.js', 
    'dependency-3.js'
  ])
}

// After build, only dependency-2.js and dependency-3.js are watched
// Changes to dependency-1.js don't trigger a rebuild
```

### Expected behavior

All transform dependencies should be watched for changes, including the first dependency in the set. When any transform dependency is modified, the build should be triggered.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
