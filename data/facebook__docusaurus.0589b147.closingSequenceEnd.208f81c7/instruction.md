# Bug Report

### Describe the bug
When using container directives with closing fences, the parser doesn't handle end-of-file (EOF) correctly. If a container directive's closing fence appears at the very end of the document without a trailing newline, the directive fails to parse properly.

### Reproduction
```markdown
:::note
Content here
:::
```

When this markdown is at the end of a file with no trailing newline character, the closing fence `:::` is not recognized, causing the directive to remain unclosed.

### Expected behavior
The parser should correctly recognize the closing fence even when it appears at EOF (when `code === null`). The directive should be properly closed and parsed regardless of whether there's a trailing newline.

### Additional context
This appears to be a regression - previously the parser would handle EOF cases correctly. The issue specifically occurs when the closing sequence is followed immediately by EOF rather than a line ending.

---
Repository: /testbed
