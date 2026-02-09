# Bug Report

### Describe the bug

I'm encountering an issue with directive parsing where directives at the end of a document or before line breaks are not being recognized correctly. The parser seems to be rejecting valid directive syntax that should be accepted.

### Reproduction

```markdown
This is a test :directive[content]
```

When the directive appears at the end of a line or document (without additional content following it), it's not being parsed as expected. The directive should be recognized and processed, but instead it appears to be treated as regular text.

### Expected behavior

Directives should be properly parsed and recognized when they appear:
- At the end of a document (when `code` is `null`)
- Before a line ending (when `markdownLineEnding(code)` returns true)

The parser should exit the directive token and continue processing normally in these cases.

### System Info
- remark-directive version: 3.0.0

---
Repository: /testbed
