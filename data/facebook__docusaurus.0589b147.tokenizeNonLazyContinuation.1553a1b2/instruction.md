# Bug Report

### Describe the bug

I'm encountering an issue with markdown parsing where lazy continuation lines in list items are being handled incorrectly. When a list item contains multiple lines where subsequent lines should be treated as part of the list item content, the parser seems to be treating them the opposite way - accepting lines that should be rejected and rejecting lines that should be accepted.

### Reproduction

```markdown
- First list item
  This should be part of the first item

- Second list item
This should NOT be part of the second item (no indentation)
```

The parser is currently treating the non-indented line as a continuation of the list item when it shouldn't be, and treating properly indented lines as separate content when they should be part of the list item.

### Expected behavior

- Lines that are properly indented (lazy continuation) should be treated as part of the list item content
- Lines without proper indentation should NOT be treated as part of the previous list item

This appears to be affecting how nested content in lists is being parsed, particularly when there are line breaks within list items.

### System Info
- remark version: 15.0.1
- Parser: micromark-based tokenizer

---
Repository: /testbed
