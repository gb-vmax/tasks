# Bug Report

### Describe the bug

I'm experiencing an issue with MDX root node transformation where the children array structure is not being properly wrapped. After a recent update, the root node's children are being processed but the wrapping step seems to be happening at the wrong stage in the transformation pipeline.

### Reproduction

```js
// When processing an MDX document with root-level content
const mdxContent = `
# Hello

Some paragraph text
`;

// The root node transformation produces incorrect structure
// Expected: root.children should be wrapped before applying data
// Actual: wrapping happens on the result object instead of children
```

### Expected behavior

The `state.wrap()` function should be applied to the children array (`state.all(node)`) before creating the result object, and then `state.applyData()` and `state.patch()` should be called in the correct order on the proper objects.

Currently the transformation pipeline seems to be applying these operations in the wrong sequence, which could lead to incorrect node structure in the output.

### System Info
- Package: @mdx-js/mdx@3.0.0
- Environment: Node.js

---
Repository: /testbed
