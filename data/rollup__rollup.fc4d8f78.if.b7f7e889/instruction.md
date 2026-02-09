# Bug Report

### Describe the bug

When trying to load a config file using the `node:` prefix syntax, the package name is being parsed incorrectly. It appears that the first character of the package name is being cut off, causing module resolution to fail.

### Reproduction

```bash
# Try to load a config from a node module
rollup --config node:my-config
```

Expected behavior: Should resolve to `rollup-config-my-config` or `my-config` package
Actual behavior: Tries to resolve `rollup-config-y-config` or `y-config` (missing the 'm')

### Steps to reproduce
1. Create a config package or use an existing one (e.g., `my-rollup-config`)
2. Try to reference it using `--config node:my-rollup-config`
3. The module resolution fails with MODULE_NOT_FOUND error

This is breaking our CI pipeline where we reference shared rollup configs from npm packages using the `node:` prefix.

### System Info
- Rollup version: latest
- Node version: 18.x
- OS: Linux

---
Repository: /testbed
