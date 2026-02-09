# Bug Report

### Describe the bug

I'm experiencing an issue where multiple emphasis nodes in markdown are sharing the same children array, causing unexpected behavior when parsing documents with multiple emphasized sections.

### Reproduction

```js
// Parse markdown with multiple emphasis elements
const markdown = `
This is *first emphasis* and this is *second emphasis*.
`;

const ast = processor.parse(markdown);
// Both emphasis nodes end up with the same children reference
// Modifying one affects the other
```

When creating multiple emphasis nodes, they all seem to reference the same underlying children array instead of having their own independent arrays. This means that if you modify the children of one emphasis node, it affects all other emphasis nodes in the document.

### Expected behavior

Each emphasis node should have its own independent children array. Modifying the children of one emphasis node should not affect other emphasis nodes.

### System Info
- remark version: 15.0.1
- Node.js version: Latest

---
Repository: /testbed
