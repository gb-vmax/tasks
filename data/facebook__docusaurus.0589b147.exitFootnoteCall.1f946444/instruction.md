# Bug Report

### Describe the bug

I'm experiencing an issue with footnote references in markdown parsing. When processing documents with footnotes, the footnote calls are not being properly handled and the document structure seems to get corrupted.

### Reproduction

```js
const markdown = `
Here's some text with a footnote[^1].

[^1]: This is the footnote content.
`;

// Parse the markdown
const result = parseMarkdown(markdown);
// The footnote reference is not properly linked
```

When I try to parse markdown containing footnote references, they don't appear in the output as expected. It seems like the footnote call tokens are being skipped during processing.

### Expected behavior

Footnote references should be properly parsed and linked to their corresponding footnote definitions. The AST should contain the correct footnote reference nodes.

### System Info
- remark-gfm version: 4.0.0
- Node version: 18.x

---
Repository: /testbed
