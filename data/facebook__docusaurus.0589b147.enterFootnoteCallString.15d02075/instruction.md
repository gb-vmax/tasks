# Bug Report

### Describe the bug

I'm experiencing an issue with footnote references in GFM (GitHub Flavored Markdown) parsing. When processing footnote calls, the label/identifier is not being captured correctly, resulting in empty or malformed footnote references.

### Reproduction

```markdown
Here's some text with a footnote[^1].

[^1]: This is the footnote content.
```

When parsing this markdown:
1. The footnote reference `[^1]` is encountered
2. The parser should capture "1" as the label
3. Instead, the label appears to be empty or not properly buffered

### Expected behavior

The footnote call should properly capture and store the label string ("1" in the example above) so that it can be correctly linked to the corresponding footnote definition. The resulting AST should have a footnoteReference node with the correct identifier and label populated.

### System Info
- remark-gfm version: 4.0.0
- Node version: Latest

This seems to affect all footnote references in documents. The footnote definitions themselves parse fine, but the inline references lose their labels during parsing.

---
Repository: /testbed
