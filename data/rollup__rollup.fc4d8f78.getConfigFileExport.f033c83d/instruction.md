# Bug Report

### Describe the bug

When running rollup in watch mode, config file changes are not being detected/reloaded properly. After modifying the rollup config file, the changes don't take effect and the old configuration continues to be used.

### Reproduction

1. Create a rollup.config.js file with some initial configuration
2. Start rollup in watch mode
3. Modify the config file (e.g., change output format or add a plugin)
4. The build continues using the old configuration instead of picking up the changes

### Expected behavior

The config file should be reloaded when it changes in watch mode, and the new configuration should be applied to subsequent builds.

### System Info
- Rollup version: latest
- Node version: 18.x
- OS: macOS

This seems to have started happening recently. The watch mode works fine for source files, but config changes are being ignored.

---
Repository: /testbed
