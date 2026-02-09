# Bug Report

### Describe the bug

When using the CLI with `--no-stdin` flag, the stdin plugin is still being added to the input options. This causes unexpected behavior where stdin is processed even when explicitly disabled.

### Reproduction

```bash
# Run rollup with stdin disabled
rollup --config --no-stdin
```

The stdin plugin gets added to the plugins array even though `stdin` is set to `false`.

### Expected behavior

When `--no-stdin` is passed (or `stdin: false` in config), the stdin plugin should not be added to the input options at all. The plugin should only be added when stdin is enabled or has a truthy value.

### System Info
- Rollup version: latest
- Node version: 18.x
- OS: Linux

---
Repository: /testbed
