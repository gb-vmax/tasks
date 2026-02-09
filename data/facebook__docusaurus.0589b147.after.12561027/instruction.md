# Bug Report

### Describe the bug

I'm experiencing an issue with markdown link parsing where the behavior seems to be inverted. When I use a link with a resource (parentheses syntax), it's being handled incorrectly based on whether the label is defined or not.

### Reproduction

```markdown
[defined label](https://example.com)
```

When the label is defined, the link with a URL in parentheses is not being processed correctly. It seems like the fallback behavior is backwards - defined labels are falling back when they should succeed, and undefined labels are succeeding when they should fall back.

### Expected behavior

Links with defined labels followed by a resource (URL in parentheses) should be processed successfully. The parser should only fall back to alternative handling when the label is not defined.

### Additional context

This affects standard markdown link syntax `[text](url)` when the text portion corresponds to a defined label. The current behavior appears to have the success/failure callbacks swapped for the resource construct attempt.

---
Repository: /testbed
