# Bug Report

### Describe the bug

I'm experiencing an issue with emphasis nodes in the markdown parser. When creating multiple emphasis elements, they seem to be sharing the same children array instead of having independent arrays. This causes content from one emphasis element to appear in other emphasis elements unexpectedly.

### Reproduction

```js
// When parsing markdown with multiple emphasis elements
const input = `*first emphasis* and *second emphasis*`;

// After parsing, both emphasis nodes reference the same children array
// Adding content to one affects the other
```

The problem appears to be that all emphasis nodes created by the compiler are referencing the same underlying children array, so modifications to one emphasis node's children will affect all other emphasis nodes.

### Expected behavior

Each emphasis node should have its own independent children array. Modifying the children of one emphasis element should not affect other emphasis elements in the document.

### System Info
- remark version: 15.0.1
- Node.js version: Latest

---
Repository: /testbed
