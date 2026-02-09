# Bug Report

### Describe the bug

I'm experiencing an issue with directive container parsing where the closing fence is not being validated correctly. It appears that directives with trailing content after the closing fence are being accepted when they should be rejected.

### Reproduction

```markdown
:::note
Some content here
::: trailing text that should not be allowed
```

The parser currently accepts this as valid, but according to the directive syntax specification, the closing fence should only be followed by whitespace or a line ending. Any other content after the closing sequence should cause the directive to be invalid.

### Expected behavior

The directive container should only be considered properly closed when the closing fence (e.g., `:::`) is followed by:
- End of file (null)
- A line ending (newline)
- Only whitespace before a line ending

Any other characters after the closing fence should invalidate the directive, and it should be parsed as regular text instead.

### Additional context

This affects the remark-directive plugin behavior and could lead to unexpected parsing results when users accidentally add content after closing fences. The current implementation seems to allow any content after the closing sequence, which doesn't match the expected directive syntax.

---
Repository: /testbed
