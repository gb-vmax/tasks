# Bug Report

### Describe the bug

I'm encountering an issue with directive container parsing where the closing fence sequence isn't being validated correctly. When using directive containers with colons (`::`), the parser seems to accept closing sequences that don't match the opening sequence length.

### Reproduction

```markdown
:::directive
content here
::
```

The above should NOT close properly since the closing sequence (`::`) has fewer colons than the opening sequence (`:::`), but it appears to be accepted anyway.

### Expected behavior

The parser should require that the closing fence sequence has at least as many colons as the opening sequence. A directive container opened with `:::` should only be closed by `:::` or longer (e.g., `::::`, `:::::`, etc.), but NOT by `::`.

This is causing issues with nested directives and content that contains shorter colon sequences that shouldn't terminate the container.

### System Info
- remark-directive version: 3.0.0

---
Repository: /testbed
