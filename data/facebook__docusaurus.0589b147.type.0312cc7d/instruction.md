# Bug Report

### Describe the bug

I'm encountering an issue with node type checking in the remark parser. When filtering or validating nodes by type, the logic appears to be inverted - nodes that should match a specific type are being rejected, while nodes that shouldn't match (or even null/undefined values) are being accepted.

### Reproduction

```js
const remark = require('remark');

// Create a parser instance
const processor = remark();

// Parse some markdown
const tree = processor.parse('# Hello\n\nThis is a paragraph.');

// Try to filter nodes by type
const headings = tree.children.filter(node => {
  // This should only return heading nodes
  return node.type === 'heading';
});

// Expected: Only heading nodes
// Actual: Returns incorrect nodes or behaves unexpectedly
console.log(headings);
```

### Expected behavior

Type checking should correctly identify nodes matching the specified type. When checking if `node.type === 'heading'`, only heading nodes should pass the check. Null or undefined values should be properly rejected.

### System Info
- remark version: 15.0.1
- Node.js version: 18.x

This seems to have broken node traversal and filtering operations that rely on type checking. Any plugins or custom code that validates node types are affected.

---
Repository: /testbed
