# Bug Report

### Describe the bug

Footnote references in GFM (GitHub Flavored Markdown) are not being parsed correctly. When trying to use footnote syntax like `[^1]`, the parser fails to recognize it properly and the footnote call doesn't render as expected.

### Reproduction

```markdown
Here's some text with a footnote reference[^1].

[^1]: This is the footnote content.
```

When parsing this markdown, the footnote reference `[^1]` is not being processed correctly. The parser seems to exit prematurely and doesn't complete the tokenization of the footnote call.

### Expected behavior

The footnote reference should be properly tokenized and rendered as a clickable link that references the footnote definition. The parser should fully process the footnote call syntax including the label marker and the identifier.

### Additional context

This appears to have broken recently. The footnote syntax was working before but now the parser is cutting off early in the tokenization process.

---
Repository: /testbed
