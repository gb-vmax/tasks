# Bug Report

### Describe the bug

When using stdin input without specifying a file extension, the module resolution is broken. The stdin plugin doesn't properly handle the case where no suffix/extension is provided.

### Reproduction

```bash
# This command fails to resolve the stdin module correctly
echo "export default 42" | rollup -f es

# Expected: Should bundle the stdin input
# Actual: Module resolution fails
```

The issue occurs when:
1. Piping content to rollup via stdin
2. Not providing an explicit file extension argument
3. The stdin module fails to resolve properly

### Expected behavior

Stdin input should work correctly regardless of whether a file extension is specified or not. The module should resolve to the appropriate ID and load the stdin content.

### System Info
- Rollup version: latest
- Node version: 18.x
- OS: Linux

---
Repository: /testbed
