# Bug Report

### Describe the bug

Markdown link parsing is broken after a recent update. Links with reference-style syntax are not being recognized correctly, and some inline links seem to be parsed incorrectly as well.

### Reproduction

```markdown
This is a [link](https://example.com) that should work.

This is a [reference link][ref] that should also work.

[ref]: https://example.com
```

When parsing the above markdown:
- Inline links with parentheses `[text](url)` may not be handled properly
- Reference-style links with brackets `[text][ref]` are failing to parse

The parser seems to be confusing which syntax is which and not matching the correct patterns.

### Expected behavior

Both inline links `[text](url)` and reference-style links `[text][ref]` should be parsed correctly and converted to proper link nodes in the AST.

### Additional context

This appears to have started happening recently. The tokenizer logic for label endings might be checking for the wrong character codes or applying the wrong fallback behavior when determining link types.

---
Repository: /testbed
