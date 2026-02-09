# Bug Report

### Describe the bug

After a recent update, footnote definitions in GFM (GitHub Flavored Markdown) are causing an infinite loop or hanging behavior when parsing. The parser seems to get stuck and never completes processing documents that contain footnote definitions.

### Reproduction

```js
const markdown = `
Here is some text with a footnote[^1].

[^1]: This is the footnote definition.
`;

// Parser hangs here and never completes
const result = parseMarkdown(markdown);
```

### Expected behavior

The parser should successfully process footnote definitions and return the parsed result without hanging or entering an infinite loop.

### System Info
- remark-gfm version: 4.0.0
- Node version: 18.x

---
Repository: /testbed
