# Bug Report

### Describe the bug

The stdin plugin is not working correctly when using file extensions with the `-` flag. When I try to bundle from stdin with a specific format like `rollup - --format es`, the input is not being loaded properly.

### Reproduction

```bash
echo "export default 42" | rollup - --format es
```

Expected: Should bundle the input from stdin
Actual: Nothing happens / no output is generated

This also affects cases where you want to specify a file extension for stdin:

```bash
echo "export default 42" | rollup -.js --format es
```

### Expected behavior

When using `-` as the input source, rollup should read from stdin and bundle it correctly, regardless of whether a file extension suffix is provided or not.

### System Info
- Rollup version: latest
- Node version: 18.x
- OS: Linux

---
Repository: /testbed
