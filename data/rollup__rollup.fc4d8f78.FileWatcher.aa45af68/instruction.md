# Bug Report

### Describe the bug

I'm experiencing an issue with file watching where transform dependencies are not being watched correctly. It seems like the watcher is registering files in the wrong category - files that should be tracked as transform dependencies are being added to the regular watchers instead, and vice versa.

### Reproduction

```js
// When watching a file as a transform dependency
watcher.watch('some-file.js', true)

// The file gets added to the wrong watcher set
// Expected: should be in transformWatchers
// Actual: ends up in regular watchers
```

This causes the build system to miss changes in transform dependencies or incorrectly trigger rebuilds for files that shouldn't cause them.

### Expected behavior

When `isTransformDependency` is `true`, the file should be added to `transformWatchers`. When it's `false`, it should be added to the regular watcher. The current behavior appears to be inverted.

### System Info
- OS: Linux/FreeBSD
- Node version: 18.x

---
Repository: /testbed
