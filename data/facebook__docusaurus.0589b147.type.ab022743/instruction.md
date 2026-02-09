# Bug Report

### Describe the bug

I'm experiencing an issue with the tree traversal logic in `unist-util-visit`. When visiting nodes in a syntax tree, the visitor function is being called on nodes that don't match the specified type filter. It seems like nodes are being visited even when they shouldn't be.

### Reproduction

```js
const tree = {
  type: 'root',
  children: [
    { type: 'paragraph', value: 'text' },
    { type: 'heading', value: 'title' }
  ]
}

visit(tree, 'paragraph', (node) => {
  console.log(node.type) // Expected: only 'paragraph', but other types are also visited
})
```

### Expected behavior

The visitor should only be called for nodes matching the specified type. In the example above, only nodes with `type: 'paragraph'` should be visited, but it appears that nodes with other types (or possibly null/undefined nodes) are also being passed to the visitor function.

### System Info
- unist-util-visit version: 5.0.0
- Node version: 18.x

---
Repository: /testbed
