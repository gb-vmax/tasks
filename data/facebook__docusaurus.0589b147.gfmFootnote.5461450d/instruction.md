# Bug Report

### Describe the bug

I'm experiencing an issue with footnote parsing in GFM (GitHub Flavored Markdown). When I try to use footnote references in my markdown content, they're not being recognized or parsed correctly. The footnote syntax appears to be broken.

### Reproduction

```markdown
Here's some text with a footnote reference[^1].

[^1]: This is the footnote content.
```

When parsing this markdown, the footnote reference `[^1]` is not being processed as expected. It seems like the parser is not correctly identifying the closing bracket of footnote references.

### Expected behavior

The parser should correctly identify and process footnote references with the `[^label]` syntax. Both the reference in the text and the footnote definition should be properly linked and rendered.

### System Info
- remark-gfm version: 4.0.0
- Using the vendored version in jest

---
Repository: /testbed
