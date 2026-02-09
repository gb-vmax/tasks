# Bug Report

### Describe the bug

I'm encountering an issue with emphasis elements in MDX content. When rendering MDX that contains emphasis (italic) text, the output is incorrect or the rendering fails completely.

### Reproduction

```js
const mdx = `
This is *emphasized text* in a paragraph.
`

// Process the MDX content
const result = await compile(mdx)
// The emphasis element is not rendered correctly
```

### Expected behavior

Emphasis elements should be properly rendered with the correct structure. The emphasized text should appear as italics in the output.

### Additional context

This seems to affect any MDX content that uses asterisks or underscores for emphasis. The issue appears to be related to how the emphasis nodes are being created in the AST.

---
Repository: /testbed
