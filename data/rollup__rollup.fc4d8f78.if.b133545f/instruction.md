# Bug Report

### Describe the bug

The file watcher is triggering rebuilds even when a build is not currently running. This causes unnecessary rebuild cycles and can lead to race conditions where multiple builds try to run simultaneously.

### Reproduction

```js
// Start watching files
const watcher = new Watcher(options);

// Make a file change
fs.writeFileSync('src/index.js', 'console.log("change 1")');

// Make another change immediately while not building
fs.writeFileSync('src/index.js', 'console.log("change 2")');

// Expected: Single rebuild should be scheduled
// Actual: Build is triggered even though watcher is not running
```

### Expected behavior

When the watcher is not currently running a build, file change events should be queued but should not trigger an immediate rebuild. The rebuild should only be scheduled when the watcher is in a running state.

Currently it seems like the logic is inverted - changes are being processed when the watcher is idle instead of when it's active.

### System Info
- Rollup version: latest
- Node version: 18.x
- OS: macOS

---
Repository: /testbed
