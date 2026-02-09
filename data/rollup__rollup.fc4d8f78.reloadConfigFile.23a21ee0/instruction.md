# Bug Report

### Describe the bug

When using watch mode with a config file, changes to the configuration file are not being applied correctly. After modifying and saving the config file, the watcher detects the change and logs "Reloading updated config..." but the new configuration doesn't actually take effect.

### Reproduction

1. Start rollup in watch mode with a config file:
```bash
rollup -c rollup.config.js -w
```

2. Make a change to `rollup.config.js` (e.g., modify output format or add a plugin)

3. Save the file

4. Observe that the console shows "Reloading updated config..." but the build continues using the old configuration

### Expected behavior

When the config file is modified, the watcher should reload and apply the new configuration settings to subsequent builds.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
