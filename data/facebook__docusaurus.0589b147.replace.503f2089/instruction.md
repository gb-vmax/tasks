# Bug Report

### Describe the bug

I'm experiencing an issue with node replacement in AST traversal when the index is `0`. It seems like nodes at index 0 in arrays are not being replaced correctly, which causes the AST transformation to fail for the first element in any node array.

### Reproduction

```js
const ast = {
  type: 'root',
  children: [
    { type: 'text', value: 'first' },
    { type: 'text', value: 'second' },
    { type: 'text', value: 'third' }
  ]
}

// Try to replace the first child (index 0)
walker.replace(ast, 'children', 0, { type: 'text', value: 'replaced' })

// The first element is not replaced as expected
// ast.children[0] still contains { type: 'text', value: 'first' }
```

### Expected behavior

When replacing a node at index 0, it should work the same way as replacing nodes at any other index. The node at position 0 should be updated with the new value.

### Additional context

This appears to affect any AST node replacement where the target is the first element in an array property. Elements at index 1, 2, etc. work fine, but index 0 behaves differently.

---
Repository: /testbed
