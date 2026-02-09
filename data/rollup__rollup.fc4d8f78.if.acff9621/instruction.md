# Bug Report

### Describe the bug

When passing plugins with inline code or key-value pairs using the `-p` flag, the plugin gets loaded twice. This causes duplicate plugin registration and can lead to unexpected behavior or errors.

### Reproduction

```bash
# Using plugin with equals sign
rollup -i input.js -o output.js -p plugin=value

# Using inline plugin code
rollup -i input.js -o output.js -p "{transform(c,i){...}}"
```

When using the `-p` flag with either `=` or `{}` characters in the plugin specification, the plugin is being registered multiple times instead of just once.

### Expected behavior

Each plugin should only be loaded and registered once, regardless of whether it contains special characters like `=` or `{}`. The command should:
- Load plugins with `=` or `{}` as-is without splitting
- Only split on commas for simple comma-separated plugin names

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
