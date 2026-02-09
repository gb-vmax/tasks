# Bug Report

### Describe the bug

When using the `--watch` flag with a config file, the watcher reloads the config even when the file content hasn't actually changed. This causes unnecessary rebuilds and "Reloading updated config..." messages to appear in the console.

### Reproduction

1. Create a rollup config file (e.g., `rollup.config.js`)
2. Run rollup with watch mode: `rollup -c -w`
3. Touch the config file without changing its content: `touch rollup.config.js`
4. Observe that rollup reloads the config and rebuilds even though nothing changed

### Expected behavior

The watcher should detect that the file content is identical and skip the reload/rebuild process. The "Reloading updated config..." message should only appear when the config file actually has different content.

### System Info

- Rollup version: latest
- Node version: 18.x
- OS: Linux/macOS

This is causing performance issues in our development workflow where file watchers or IDEs sometimes trigger file change events even when the content hasn't changed.

---
Repository: /testbed
