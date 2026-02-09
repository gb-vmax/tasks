# Bug Report

### Describe the bug
Footnote references in GFM (GitHub Flavored Markdown) are not being parsed correctly. When using the footnote syntax `[^1]`, the parser appears to exit prematurely and doesn't process the footnote call properly.

### Reproduction
```markdown
Here is some text with a footnote reference[^1].

[^1]: This is the footnote content.
```

When parsing this markdown, the footnote reference is not recognized or linked to its corresponding footnote definition.

### Expected behavior
The parser should correctly identify and process footnote calls like `[^1]` and link them to their definitions. The footnote reference should be parsed as a complete `gfmFootnoteCall` token.

### System Info
- remark-gfm version: 4.0.0
- Node version: Latest

---
Repository: /testbed
