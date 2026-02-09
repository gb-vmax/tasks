# Bug Report

### Describe the bug

I'm experiencing an issue with GitHub Flavored Markdown (GFM) footnote definitions. When parsing markdown with footnotes, the parser seems to get stuck or doesn't properly close the footnote definition block, causing subsequent content to be incorrectly parsed as part of the footnote.

### Reproduction

```markdown
[^1]: This is a footnote definition.
It can span multiple lines.

This should be regular paragraph text, not part of the footnote.
```

When parsing this markdown, the regular paragraph text after the footnote gets incorrectly included as part of the footnote definition instead of being treated as separate content.

### Expected behavior

The footnote definition should be properly closed after its content ends, and subsequent paragraphs should be parsed as separate block elements, not as continuations of the footnote definition.

### System Info
- remark-gfm version: 4.0.0
- Node version: Latest

---
Repository: /testbed
