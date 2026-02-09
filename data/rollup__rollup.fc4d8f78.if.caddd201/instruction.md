# Bug Report

### Describe the bug

When using the watch mode with `--watch` flag, the initial heading is not being displayed in the terminal. The screen reset functionality seems to be skipping the first output, so users don't see any heading when the watcher starts up.

### Reproduction

```bash
# Run rollup in watch mode
rollup -c --watch
```

Expected: The initial heading should be displayed when the watcher starts
Actual: No heading is displayed on the first run, only on subsequent rebuilds

### Steps to reproduce
1. Start rollup in watch mode
2. Observe that no initial heading appears in the terminal
3. Make a change to trigger a rebuild
4. Now the heading appears

### Expected behavior
The heading should be displayed on the first run when the watcher initializes, not just on subsequent rebuilds. This is important for users to know that the watcher has started successfully.

### System Info
- Rollup version: latest
- Node version: 18.x
- OS: macOS

---
Repository: /testbed
