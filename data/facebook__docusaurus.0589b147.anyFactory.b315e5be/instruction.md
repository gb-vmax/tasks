# Bug Report

### Describe the bug

I'm experiencing an issue with the tree traversal logic where nodes that shouldn't match are being visited. It seems like the visitor function is being called on nodes that don't meet the specified criteria.

### Reproduction

```js
const tree = {
  type: 'root',
  children: [
    { type: 'paragraph', value: 'text' },
    { type: 'heading', value: 'title' },
    { type: 'code', value: 'example' }
  ]
}

// Only want to visit 'paragraph' nodes
visit(tree, 'paragraph', (node) => {
  console.log(node.type)
})

// Expected: Only logs 'paragraph'
// Actual: Logs all node types including 'heading' and 'code'
```

### Expected behavior

The visit function should only call the visitor callback for nodes that match the specified type. When I specify `'paragraph'` as the test, only paragraph nodes should be visited, not all nodes in the tree.

### Additional context

This seems to have started recently. The visitor is being called for every node regardless of the test criteria I provide. Even when using multiple test conditions, nodes that don't match any of them are still being visited.

---
Repository: /testbed
