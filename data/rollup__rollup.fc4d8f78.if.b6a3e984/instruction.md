# Bug Report

### Describe the bug

When passing a custom config file path to the CLI (e.g., `--config my-config.js`), Rollup fails to resolve the path correctly. It seems like the config path is not being handled properly and the build fails with a "cannot find config file" error.

### Reproduction

```bash
# This doesn't work as expected
rollup --config ./configs/rollup.config.js

# Error: Could not resolve config file path
```

The issue occurs when trying to use a config file that's not in the current working directory or when specifying a relative/absolute path.

### Expected behavior

Rollup should be able to resolve and use the config file at the specified path. When I provide `--config ./configs/rollup.config.js`, it should load that exact file instead of searching for a default config.

### System Info
- Rollup version: latest
- Node version: 18.x
- OS: macOS

---
Repository: /testbed
