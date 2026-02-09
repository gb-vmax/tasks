# Bug Report

### Describe the bug

I'm encountering an issue with footnote definitions in GFM (GitHub Flavored Markdown) parsing. When processing markdown documents that contain footnote definitions, the parser seems to get stuck or produces malformed output. The footnotes aren't being properly closed in the AST, which causes downstream processing to fail.

### Reproduction

```markdown
Here is some text with a footnote[^1].

[^1]: This is the footnote definition.

More text after the footnote.
```

When parsing this markdown, the footnote definition node doesn't get properly exited, leading to an incorrectly structured AST. This causes issues when trying to traverse or transform the tree afterwards.

### Expected behavior

The footnote definition should be properly closed in the AST, with all child nodes correctly nested inside it. The parser should continue processing the rest of the document normally after the footnote definition ends.

### System Info
- remark-gfm version: 4.0.0
- Node version: 18.x

---
Repository: /testbed
