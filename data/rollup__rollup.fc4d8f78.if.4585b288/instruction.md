# Bug Report

### Describe the bug

When using the CLI watch mode, the screen reset/heading output is not displaying on the first run. The heading message that should appear when the watcher starts is completely missing, and it only shows up on subsequent file changes.

### Reproduction

1. Start rollup in watch mode with `--watch` flag
2. Observe that no heading is printed when the watcher initially starts
3. Make a change to a watched file
4. Now the heading appears (but it shouldn't on subsequent runs)

The expected behavior is that the heading should be displayed on the first run when the watcher starts, and then be suppressed on subsequent rebuilds.

### Expected behavior

The heading should be printed to stderr on the very first run when starting the watch mode, before any file changes occur.

### System Info
- Rollup version: latest
- Node version: 18.x
- OS: macOS

---
Repository: /testbed
