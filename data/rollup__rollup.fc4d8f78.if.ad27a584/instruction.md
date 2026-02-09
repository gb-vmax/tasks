# Bug Report

### Describe the bug

When using the CLI with `--stdin` flag set to `false`, the stdin plugin is still being added to the input options. This causes unexpected behavior where stdin input is processed even when explicitly disabled.

### Reproduction

```bash
# Run rollup with stdin disabled
rollup --stdin=false --input src/main.js

# stdin plugin is still active and processes input
# Expected: stdin plugin should not be added when --stdin=false
```

The issue appears to be related to how the `stdin` command option is being checked. When `stdin` is set to `false`, it should skip adding the stdin plugin entirely, but currently it's being added anyway.

### Expected behavior

When `--stdin=false` is passed, the stdin plugin should not be added to the input options. Only when stdin is explicitly enabled or not set to false should the plugin be included.

### System Info
- Rollup version: latest
- Node version: 18.x
- OS: Linux

---
Repository: /testbed
