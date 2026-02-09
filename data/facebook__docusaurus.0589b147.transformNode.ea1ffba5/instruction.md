# Bug Report

### Describe the bug

I'm experiencing an issue with MDX content rendering where certain node properties are not being properly transformed. It seems like the first property of the original node is not being deleted and the last property of the new node is not being copied over during node transformation.

### Reproduction

When processing MDX files with custom remark plugins that transform AST nodes, the transformed nodes are missing properties or retain old properties they shouldn't have.

For example:
```js
// Original node has properties: ['type', 'value', 'position']
// New node has properties: ['type', 'children', 'data']

// After transformation:
// Expected: node should have ['type', 'children', 'data']
// Actual: node has ['type', 'children'] (missing 'data', still has 'type' from original)
```

This causes MDX content to render incorrectly or fail to process entirely, especially when dealing with complex transformations that rely on all properties being correctly transferred.

### Expected behavior

All properties from the original node should be removed and all properties from the new node should be copied over completely during the transformation process.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
