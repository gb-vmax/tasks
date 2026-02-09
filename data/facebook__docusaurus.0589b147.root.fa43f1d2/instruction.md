# Bug Report

### Describe the bug

After a recent update, MDX root node transformation seems to be applying operations in the wrong order. The wrapping behavior for root-level content appears to have changed, and now the structure of the transformed output is different than expected.

### Reproduction

When processing an MDX document with root-level content:

```js
const mdx = `
# Hello

This is a paragraph at root level.
`;

// Process the MDX
const result = await compile(mdx);
```

The resulting HAST structure has the wrapping applied at a different level than before. Previously, the children were wrapped first, then the data transformations were applied. Now it seems the order has been reversed, which affects how root-level content is structured in the output.

### Expected behavior

The root node's children should be wrapped before applying data transformations and patching, maintaining the correct nesting structure for root-level content. The transformation pipeline should follow the same order as previous versions to ensure consistent output.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
