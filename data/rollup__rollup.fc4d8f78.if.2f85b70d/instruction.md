# Bug Report

### Describe the bug

The `--stdin` flag behavior seems to be inverted. When I explicitly set `--stdin=false`, the stdin plugin is still being added, and when I don't specify the flag or set it to true, the plugin is not being added.

### Reproduction

```bash
# This should NOT use stdin but it does
rollup --stdin=false input.js

# This SHOULD use stdin but doesn't
rollup --stdin input.js
```

The stdin plugin is being added when it shouldn't be and vice versa.

### Expected behavior

When `--stdin=false` is specified, the stdin plugin should not be added. When `--stdin` is true or not specified (assuming stdin is enabled by default), the stdin plugin should be added to handle input from stdin.

### System Info
- Rollup version: latest
- Node version: 18.x
- OS: Linux

---
Repository: /testbed
