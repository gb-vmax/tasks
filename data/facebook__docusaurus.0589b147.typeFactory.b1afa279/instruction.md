# Bug Report

### Describe the bug

I'm experiencing an issue with node type checking in the remark parser. When filtering or validating nodes by their type, the behavior seems inverted - nodes that should match a specific type are being excluded, and nodes that shouldn't match are being included.

### Reproduction

```js
// Trying to filter nodes by type
const headingNodes = nodes.filter(typeFactory('heading'));

// Expected: Only heading nodes
// Actual: Everything EXCEPT heading nodes
```

This is causing problems when trying to process specific node types in markdown AST transformations. For example, when I try to extract all headings from a document, I get everything but the headings.

### Expected behavior

When using `typeFactory('heading')`, it should return a function that matches nodes with `type === 'heading'`, not nodes where the type is different.

### System Info
- remark version: 15.0.1
- Node.js version: Latest

---
Repository: /testbed
