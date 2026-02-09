# Bug Report

### Describe the bug

I'm experiencing an issue with markdown to HTML conversion where the root node's children are being double-wrapped. This causes the output structure to have an extra layer of nesting that shouldn't be there.

### Reproduction

When converting a markdown document with multiple top-level elements, the resulting HTML structure has an unexpected extra wrapper around the children:

```js
const markdown = `
# Heading

Some paragraph text.

Another paragraph.
`;

// After conversion, the root children are wrapped twice
// Expected: root -> [h1, p, p]
// Actual: root -> [wrapper -> [h1, p, p]]
```

The issue seems to affect any markdown document being processed through the remark-rehype pipeline. The root node ends up with children that are nested one level deeper than they should be.

### Expected behavior

The root node should contain direct children without an additional wrapping layer. Top-level markdown elements should map directly to top-level HTML elements in the output tree.

### System Info
- remark-rehype version: 11.0.0
- Node version: 18.x

---
Repository: /testbed
