# Bug Report

### Describe the bug

I'm experiencing an issue with node type checking in the remark parser. When filtering or validating nodes by their type, the logic appears to be inverted - nodes that should match a specific type are being rejected, and nodes that shouldn't match are being accepted.

### Reproduction

```js
const tree = {
  type: 'paragraph',
  children: [
    { type: 'text', value: 'Hello' }
  ]
}

// Checking if a node is a paragraph
const isParagraph = typeFactory('paragraph')
console.log(isParagraph(tree)) // Returns false, but should return true

// This also affects filtering operations
const paragraphs = findAll(tree, typeFactory('paragraph'))
// Returns nodes that are NOT paragraphs instead of paragraphs
```

### Expected behavior

The `typeFactory` function should return `true` when a node's type matches the specified check value, and `false` when it doesn't match. Currently it's doing the opposite.

This is breaking any code that relies on type-based node filtering or validation in the AST.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
