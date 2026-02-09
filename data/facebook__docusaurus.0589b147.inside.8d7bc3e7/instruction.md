# Bug Report

### Describe the bug

I'm experiencing issues with emphasis/strong emphasis parsing in markdown when using underscores (`_`). The parser seems to be incorrectly handling the opening and closing of underscore-delimited emphasis markers.

### Reproduction

When trying to parse markdown with underscore emphasis, the behavior is inconsistent:

```markdown
This _should be emphasized_ text.
This __should be strong__ text.
```

The parser appears to be treating underscore markers differently than asterisk markers (`*`), even though they should behave similarly according to the CommonMark spec. The issue seems related to how the parser determines which sequences can open or close emphasis spans.

### Expected behavior

Underscore-delimited emphasis should work the same way as asterisk-delimited emphasis. Both `_text_` and `*text*` should produce emphasized text, and both `__text__` and `**text**` should produce strong emphasis.

### Additional context

This appears to affect the tokenization logic for attention sequences (emphasis/strong). The problem manifests when the parser tries to determine whether an underscore sequence can open or close an emphasis span based on the surrounding characters.

---
Repository: /testbed
