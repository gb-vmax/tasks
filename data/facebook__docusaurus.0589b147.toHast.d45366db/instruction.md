# Bug Report

### Describe the bug

I'm experiencing an issue with footnote rendering in MDX documents. When footnotes are present in the document, they appear at the wrong position in the output - specifically, they're being inserted at the beginning of the document instead of at the end where they should be.

### Reproduction

```js
const mdx = `
# My Document

Some content with a footnote[^1].

More content here.

[^1]: This is the footnote text.
`

// Process the MDX
const result = await compile(mdx)

// The footnote section appears at the top instead of the bottom
```

### Expected behavior

Footnotes should be rendered at the end of the document, after all the main content. Currently they're appearing at the beginning, which breaks the expected document structure.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
