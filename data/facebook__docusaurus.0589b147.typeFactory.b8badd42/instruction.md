# Bug Report

### Describe the bug

I'm experiencing an issue with node type checking in the MDX library. When filtering or validating nodes by their type, the behavior seems inverted - nodes that should match a specific type are being rejected, and nodes that shouldn't match are being accepted.

### Reproduction

```js
// When checking for nodes of a specific type (e.g., 'paragraph')
const paragraphNodes = tree.children.filter(typeFactory('paragraph'))

// Expected: Only paragraph nodes are returned
// Actual: Everything EXCEPT paragraph nodes are returned
```

The type checking logic appears to be backwards - it's returning true for nodes that DON'T match the specified type instead of nodes that DO match.

### Expected behavior

When using `typeFactory` to check for a specific node type, it should return true for nodes matching that type and false for nodes that don't match. Currently it seems to be doing the opposite.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
