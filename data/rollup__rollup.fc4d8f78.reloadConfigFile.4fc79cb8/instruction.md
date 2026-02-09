# Bug Report

### Describe the bug

When running rollup in watch mode with a config file, changes to the config file are not being reloaded properly. After modifying the rollup config and saving it, the watcher detects the change and logs "Reloading updated config..." but the new configuration doesn't actually take effect. The build continues using the old configuration settings.

### Reproduction

1. Create a rollup config file (e.g., `rollup.config.js`)
2. Start rollup in watch mode: `rollup -c -w`
3. Modify the config file (change output format, add a plugin, etc.)
4. Save the config file
5. Observe that the console shows "Reloading updated config..." but the build output still uses the old configuration

### Expected behavior

When the config file is modified and saved, rollup should reload the configuration and apply the new settings to subsequent builds. The watcher should use the updated configuration options immediately after detecting the config file change.

### System Info
- Rollup version: latest
- Node version: 18.x
- OS: macOS

---
Repository: /testbed
