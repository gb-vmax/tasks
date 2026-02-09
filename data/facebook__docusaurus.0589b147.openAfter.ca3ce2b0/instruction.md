# Bug Report

### Describe the bug

I'm experiencing an issue with directive container parsing in remark-directive. When a directive container fence is followed by `null` (end of file), the parser doesn't handle it correctly and fails to properly close the container.

### Reproduction

```markdown
:::note
This is a note directive
```

When the directive container is at the end of the file without a closing fence and followed by EOF, the parsing behavior is incorrect. The container should be properly closed when encountering `null` (EOF), but instead it seems to be taking the wrong code path.

### Expected behavior

The directive container should be properly closed and exited when reaching the end of file, even if there's no explicit closing fence. The parser should handle the `null` case (EOF) correctly in the `openAfter` function.

### System Info
- remark-directive version: 3.0.0
- Node version: Latest

---
Repository: /testbed
