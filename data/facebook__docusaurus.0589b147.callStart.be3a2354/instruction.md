# Bug Report

### Describe the bug

Footnote references in GFM (GitHub Flavored Markdown) are not being parsed correctly. When trying to use footnote syntax like `[^1]`, the parser fails to recognize it as a valid footnote reference.

### Reproduction

```js
const markdown = `
Here is some text with a footnote reference[^1].

[^1]: This is the footnote content.
`

// Parse the markdown
const result = parseMarkdown(markdown)

// Footnote reference is not recognized
console.log(result) // Expected footnote node is missing
```

### Expected behavior

The parser should correctly identify and process footnote references that start with `[^` followed by the footnote identifier. The footnote call should be properly tokenized and included in the AST.

### System Info
- remark-gfm version: 4.0.0
- Node version: 18.x

This seems to have broken recently as footnotes were working in earlier versions. The parser appears to be rejecting valid footnote syntax.

---
Repository: /testbed
