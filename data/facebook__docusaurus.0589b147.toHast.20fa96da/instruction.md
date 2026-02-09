# Bug Report

### Describe the bug

I'm experiencing an issue with MDX rendering where the document structure appears to be malformed. When processing MDX content that includes footnotes, the resulting AST (Abstract Syntax Tree) has an incorrect structure - the root node seems to be getting the wrong type, and footnotes are appearing in the wrong position in the document.

### Reproduction

```js
// Processing MDX content with footnotes
const mdxContent = `
# Hello World

Some text with a footnote[^1]

[^1]: This is a footnote
`;

const result = toHast(tree, options);
// The result structure is not what's expected
// - Root node type is incorrect when dealing with arrays
// - Footnotes appear at the beginning instead of the end
```

### Expected behavior

- When the processed node is an array, it should be wrapped in a root node with `children` property
- Footnotes should be appended to the end of the document (after the main content)
- The document structure should maintain proper ordering: content first, then footnotes

### Actual behavior

- The root node wrapping logic appears inverted
- Footnotes are being prepended to the beginning of the document instead of appended to the end

This is affecting the final rendered output where footnotes show up before the main content, which breaks the expected document flow.

### System Info
- @mdx-js/mdx version: 3.0.0

---
Repository: /testbed
