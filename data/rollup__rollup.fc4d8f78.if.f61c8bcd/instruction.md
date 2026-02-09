# Bug Report

### Describe the bug

After making some changes to my project, I noticed that the file watcher is behaving strangely. Files that should no longer be watched are still being monitored, and I'm getting unnecessary rebuild triggers when modifying files that aren't part of my current bundle anymore.

### Reproduction

```js
// Initial build with file A
rollup({
  input: 'index.js',
  // index.js imports fileA.js
})

// Update to remove fileA from dependency graph
// (e.g., remove the import statement)

// Modify fileA.js
// Expected: No rebuild triggered
// Actual: Rebuild is triggered even though fileA is no longer used
```

### Steps to reproduce
1. Start rollup in watch mode with a set of files
2. Modify your code to remove a dependency (so a file is no longer imported)
3. Edit the file that was removed from the dependency graph
4. Observe that rollup still triggers a rebuild

### Expected behavior

When a file is removed from the dependency graph (no longer imported), the file watcher should stop watching that file. Changes to unwatched files should not trigger rebuilds.

### System Info
- Rollup version: latest
- Node version: 18.x
- OS: macOS

This seems like it might be a regression as I don't remember seeing this behavior in earlier versions. The watcher appears to be keeping references to files it should have released.

---
Repository: /testbed
