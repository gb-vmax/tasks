# Bug Report

### Describe the bug

When using the `--config node:` prefix to load external config packages, the fallback resolution is broken. If the prefixed package name (e.g., `rollup-config-mypackage`) isn't found, the CLI tries to resolve the wrong package name instead of the original one.

### Reproduction

```bash
# Install a custom config package
npm install my-custom-config

# Try to use it with node: prefix
rollup --config node:my-custom-config
```

When `rollup-config-my-custom-config` doesn't exist, it should fall back to resolving `my-custom-config`, but instead it tries to resolve something else and fails.

### Expected behavior

The CLI should:
1. First try to resolve `rollup-config-{packageName}`
2. If that fails, fall back to resolving `{packageName}` (the original package name after `node:`)
3. Show appropriate error message if neither can be found

### System Info
- Rollup version: latest
- Node version: 18.x
- OS: Linux

---
Repository: /testbed
