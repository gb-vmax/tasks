# Bug Report

### Describe the bug

When running rollup CLI without explicitly setting the `--stdin` flag, the stdin plugin is no longer being loaded by default. This breaks workflows that previously relied on piping input to rollup without needing to specify `--stdin=true`.

### Reproduction

```bash
# This used to work but no longer does
echo "export default 42" | rollup -f es

# Now requires explicit flag
echo "export default 42" | rollup --stdin -f es
```

The stdin plugin should be active by default (when stdin is not explicitly disabled), but it appears to only activate when `stdin` is explicitly set to a truthy value.

### Expected behavior

The stdin plugin should be loaded when:
- `--stdin` flag is passed (explicitly enabled)
- No `--stdin=false` flag is passed (default behavior)

It should only be disabled when `--stdin=false` is explicitly set.

### System Info
- Rollup version: latest
- Node version: 18.x
- OS: Linux

---
Repository: /testbed
