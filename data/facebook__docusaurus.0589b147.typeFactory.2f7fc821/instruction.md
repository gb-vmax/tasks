# Bug Report

### Describe the bug

I'm experiencing an issue with node type checking in the remark parser. When filtering or checking for specific node types, the logic appears to be inverted - nodes that should match a specific type are being rejected, while nodes that shouldn't match are being accepted.

### Reproduction

```js
// Trying to filter nodes by type
const processor = remark();
const tree = processor.parse('# Heading\n\nParagraph text');

// Check for heading nodes
const headings = tree.children.filter(node => node.type === 'heading');
// Expected: should find the heading node
// Actual: returns empty array or incorrect nodes
```

When using type checking functions to validate or filter nodes by their type property, the matching behavior is reversed. Nodes with the correct type are excluded while nodes with different types are included.

### Expected behavior

Type checking should return `true` when a node's type matches the expected type, and `false` when it doesn't match. Currently it seems to be doing the opposite.

### System Info
- remark version: 15.0.1
- Node.js version: 18.x

---
Repository: /testbed
