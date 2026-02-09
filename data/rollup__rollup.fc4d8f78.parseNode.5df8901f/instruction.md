# Bug Report

### Describe the bug

I'm experiencing an issue with dynamic imports where the `sourceAstNode` property is being set before the parent class's `parseNode` method is called. This causes the source node to be incorrectly assigned or potentially overwritten during parsing.

### Reproduction

```js
// When parsing an import expression like:
import('./module.js')

// The sourceAstNode gets set before super.parseNode() completes
// This can lead to incorrect AST node references
```

The problem occurs during the AST parsing phase where the order of operations matters. The source node should be assigned after the parent parsing is complete, not before.

### Expected behavior

The `sourceAstNode` should be properly set after the parent class has finished its parsing operations to ensure all node properties are correctly initialized.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
