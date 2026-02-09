# Bug Report

### Describe the bug

When using the `--config node:` prefix to load external config packages, the CLI fails to properly resolve the package name. After the prefix is stripped, the resolution logic appears to be using an incorrect substring index, causing the package lookup to fail.

### Reproduction

```bash
# Try to load a config package using the node: prefix
rollup --config node:my-config

# Expected: Should try to resolve 'rollup-config-my-config' first, then fall back to 'my-config'
# Actual: Fails to resolve the correct package name
```

### Steps to reproduce
1. Create or use an existing npm package for rollup configuration (e.g., `my-rollup-config`)
2. Try to reference it using `--config node:my-rollup-config`
3. The package resolution fails even though the package exists in node_modules

### Expected behavior

The CLI should:
1. First attempt to resolve `rollup-config-<packageName>` 
2. If that fails, fall back to resolving `<packageName>` directly
3. If both fail with MODULE_NOT_FOUND, show the appropriate error message

The package name extraction after the `node:` prefix should preserve the full package name for the fallback resolution.

### System Info
- Rollup version: latest
- Node version: 18.x
- OS: Linux

---
Repository: /testbed
