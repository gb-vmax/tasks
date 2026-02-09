# Bug Report

### Describe the bug

The stdin plugin is not working correctly when using file extensions. When I try to use `rollup -c` with stdin input and specify a file extension (e.g., `-=.js`), the plugin fails to load the content from stdin.

### Reproduction

```bash
echo "export default 42" | rollup -c --format es -=.js
```

The build fails because the stdin content is not being loaded when an extension is specified.

### Expected behavior

The stdin plugin should handle both cases:
1. Loading from `-` (stdin without extension)
2. Loading from `-.extension` (stdin with a specific extension like `-.js`, `-.ts`, etc.)

Both should read and return the content from stdin.

### System Info
- Rollup version: latest
- Node version: 18.x
- OS: Linux

---
Repository: /testbed
