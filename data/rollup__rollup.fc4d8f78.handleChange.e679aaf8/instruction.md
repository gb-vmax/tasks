# Bug Report

### Describe the bug

I'm experiencing an issue with file watching on Linux/FreeBSD systems where transform dependencies (like preprocessors or custom transformers) are not being properly tracked after file changes. When a file is modified and then immediately recreated, the watcher seems to be tracking the wrong file ID internally.

### Reproduction

```js
// Setup a file watcher with a transform dependency
const watcher = new FileWatcher({
  // ... config
});

// Watch a file that goes through a transformer
watcher.watch('input.scss', { transformWatcherId: 'output.css' });

// Now modify and recreate the file (common on Linux)
// 1. Delete input.scss
// 2. Immediately recreate input.scss with new content

// Expected: watcher should track changes to 'output.css' (the transform result)
// Actual: watcher appears to be invalidating 'input.scss' instead
```

### Expected behavior

When using `transformWatcherId`, the file watcher should:
1. Unwatch and re-add the transformed file ID (not the original file ID) on Linux/FreeBSD
2. Invalidate the transformed file ID (not the original file ID) when changes occur

This is critical for build tools that use transforms/preprocessors where the source file and output file have different paths.

### System Info
- OS: Linux / FreeBSD
- File watcher: chokidar

The issue appears to be specific to Linux and FreeBSD platforms where the unwatch/watch workaround is applied.

---
Repository: /testbed
