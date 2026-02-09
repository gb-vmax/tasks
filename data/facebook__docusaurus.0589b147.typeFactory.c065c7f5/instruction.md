# Bug Report

Title: Node type checking returns incorrect results for valid nodes

I've encountered an issue where node type validation is failing for valid nodes in the AST. When checking if a node matches a specific type, the validation returns unexpected results.

### Reproduction
```js
const node = {
  type: 'paragraph',
  children: []
}

// This should return true but returns false
const isParagraph = is(node, 'paragraph')
```

The type check seems to be inverted or broken - it's returning false for nodes that should match and possibly true for nodes that shouldn't match.

### Expected behavior
When a node's type property matches the expected type, the type check should return `true`. When it doesn't match, it should return `false`.

### Additional context
This appears to affect any code that uses type checking for AST nodes. The issue causes nodes to be incorrectly filtered or skipped during tree traversal and transformation operations.

---
Repository: /testbed
