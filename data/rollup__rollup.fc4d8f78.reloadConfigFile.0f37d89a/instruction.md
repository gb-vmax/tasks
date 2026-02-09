# Bug Report

### Describe the bug

When using watch mode with a config file, the config doesn't reload properly when the file is changed. The watcher detects the change but the new configuration is never applied - it seems like the reload is being cancelled prematurely.

### Reproduction

1. Start rollup in watch mode with a config file:
```bash
rollup -c rollup.config.js -w
```

2. Make a change to `rollup.config.js` (e.g., modify an output option)

3. Save the file

4. The console shows "Reloading updated config..." but the actual config changes are not applied

5. The build continues using the old configuration

### Expected behavior

When the config file changes, the watcher should:
1. Detect the change
2. Reload the configuration
3. Close the existing watcher
4. Restart with the new configuration options

Instead, it appears the reload is being skipped/cancelled even though the file has actually changed.

### System Info
- Rollup version: latest
- Node version: 18.x
- OS: macOS

This is blocking our development workflow since we need to manually restart the watch process every time we change the config.

---
Repository: /testbed
