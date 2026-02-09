# Bug Report

### Describe the bug

I'm experiencing an issue with node type checking in the remark parser. When processing markdown AST nodes, the type validation is not working as expected - it's accepting nodes that shouldn't match the specified type.

### Reproduction

```js
// Create a node with a specific type
const node = {
  type: 'paragraph',
  children: []
}

// Check if node matches 'heading' type
// This incorrectly returns true when it should return false
const isHeading = typeFactory('heading')
console.log(isHeading(node)) // Expected: false, Got: true
```

Also seeing weird behavior when passing `null` or `undefined`:

```js
const checker = typeFactory('text')
console.log(checker(null)) // Returns true instead of false
console.log(checker(undefined)) // Returns true instead of false
```

### Expected behavior

The type checker should:
1. Return `false` when the node's type doesn't match the expected type
2. Return `false` when passed `null` or `undefined` instead of a valid node

### System Info
- remark version: 15.0.1
- Node.js version: 18.x

This is causing issues in my markdown processing pipeline where nodes are being incorrectly identified and processed.

---
Repository: /testbed
