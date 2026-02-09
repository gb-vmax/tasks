# Bug Report

### Describe the bug

When running in watch mode, file changes that occur while a build is already in progress are not being properly queued for rebuilding. The watcher seems to miss changes and doesn't trigger a rebuild after the current build completes, even though files were modified during the build process.

### Reproduction

1. Start the watcher with a project that has a slow build time
2. Make a file change that triggers a build
3. While the build is running, make another change to the same or different file
4. Wait for the first build to complete

Expected: A second build should automatically start after the first one finishes
Actual: No rebuild is triggered, the changed files are ignored

### Steps to reproduce

```js
// Start watch mode
const watcher = watch({
  input: 'src/index.js',
  output: { file: 'dist/bundle.js' }
});

// Simulate:
// 1. Initial change triggers build
// 2. Make another change while build is in progress
// 3. First build completes but second change is not picked up
```

### Expected behavior

The watcher should queue up changes that happen during an active build and automatically trigger a new build once the current one finishes. All file modifications should be captured and processed.

### System Info
- Rollup version: latest
- OS: macOS
- Node: v18.x

---
Repository: /testbed
