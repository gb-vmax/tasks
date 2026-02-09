# Bug Report

### Describe the bug

Footnote references in GFM (GitHub Flavored Markdown) are not being parsed correctly. The syntax `[^1]` for footnote calls doesn't work as expected - it appears to be treated as regular text instead of being recognized as a footnote reference.

### Reproduction

```markdown
Here is some text with a footnote reference[^1].

[^1]: This is the footnote content.
```

When parsing this markdown, the `[^1]` reference is not being converted to a proper footnote link. It just renders as plain text.

### Expected behavior

The `[^1]` syntax should be recognized as a footnote reference and properly linked to the corresponding footnote definition `[^1]:`. This is standard GFM footnote syntax and was working in previous versions.

### Additional context

This seems to have broken recently. The footnote definitions themselves might still work, but the inline references using `[^note]` syntax are not being tokenized properly.

---
Repository: /testbed
