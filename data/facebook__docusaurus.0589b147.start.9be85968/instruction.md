# Bug Report

### Describe the bug

Footnote references in GFM (GitHub Flavored Markdown) are not being parsed correctly. When I try to use footnote syntax like `[^1]`, the footnote call is not recognized and doesn't render as expected.

### Reproduction

```markdown
Here's some text with a footnote reference[^1].

[^1]: This is the footnote content.
```

When parsing this markdown, the footnote reference `[^1]` is not being recognized properly. The parser seems to exit the footnote call token immediately without processing the actual footnote label.

### Expected behavior

The footnote reference should be parsed completely, including the label marker and the label content itself. The output should properly link the reference to the footnote definition.

### System Info
- remark-gfm version: 4.0.0

---
Repository: /testbed
