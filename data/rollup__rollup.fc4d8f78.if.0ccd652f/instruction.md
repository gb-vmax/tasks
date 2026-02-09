# Bug Report

### Describe the bug

When using the `node:` prefix to load external config files, the config path resolution is broken. The package name is being parsed incorrectly, causing module resolution to fail.

### Reproduction

```bash
# Try to load a config using the node: prefix
rollup --config node:my-config
```

Expected: Should resolve to `rollup-config-my-config` or `my-config` package
Actual: Module not found error

The issue appears to be with how the package name is extracted from the `node:` prefixed string. When I use `node:my-config`, it seems like the first character of the package name is being cut off during parsing.

### Steps to reproduce

1. Create a config package (e.g., `rollup-config-test` or just `test`)
2. Try to load it using `--config node:test`
3. The module resolution fails even though the package exists

### Expected behavior

The config file should be resolved correctly from the external package when using the `node:` prefix syntax.

### System Info
- Rollup version: latest
- Node version: 18.x
- OS: macOS

---
Repository: /testbed
