# Bug Report

### Describe the bug

I'm encountering an issue with directive container parsing where the closing fence is not being recognized correctly. It seems like containers that should be properly closed are being treated as invalid, and vice versa.

### Reproduction

```markdown
:::note
This is a container directive
:::
```

When parsing the above markdown with directive containers, the closing `:::` fence is not being matched properly. The parser seems to be rejecting valid closing sequences or accepting invalid ones.

### Expected behavior

The directive container should be properly closed when encountering a valid closing fence (three or more colons followed by a line ending or EOF). The parser should correctly identify when a closing sequence is valid and when it's not.

### System Info
- remark-directive version: 3.0.0
- Parser: remark

---
Repository: /testbed
