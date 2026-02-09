# Bug Report

### Describe the bug

Footnote references in GFM (GitHub Flavored Markdown) are not being parsed correctly. When using the standard footnote syntax `[^1]`, the parser fails to recognize them as footnote calls.

### Reproduction

```markdown
Here is some text with a footnote reference[^1].

[^1]: This is the footnote content.
```

When parsing this markdown, the footnote reference `[^1]` is not being tokenized as a footnote call. The parser seems to be skipping the tokenization step entirely.

### Expected behavior

The parser should correctly identify `[^1]` as a footnote reference and process it accordingly. The footnote syntax is a standard part of GFM and should work out of the box.

### System Info
- remark-gfm version: 4.0.0

---
Repository: /testbed
