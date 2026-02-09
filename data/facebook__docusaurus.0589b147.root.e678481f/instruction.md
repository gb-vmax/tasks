# Bug Report

### Describe the bug

I'm experiencing an issue with the markdown to HTML conversion where the root node seems to be getting double-wrapped. When converting markdown documents, the resulting HTML structure has an extra layer of wrapping that shouldn't be there.

### Reproduction

```js
// Convert a simple markdown document
const markdown = `
# Hello World

This is a test paragraph.
`;

const result = convertMarkdownToHtml(markdown);

// The root children are wrapped twice instead of once
// Expected: { type: 'root', children: [/* direct children */] }
// Actual: { type: 'root', children: [[/* nested children */]] }
```

### Expected behavior

The root node should have its children wrapped once by `state.wrap()`, not twice. The current behavior creates an unnecessary extra level of nesting in the output tree.

### System Info
- remark-rehype version: 11.0.0
- Node version: 18.x

---
Repository: /testbed
