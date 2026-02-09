# Bug Report

### Describe the bug

I'm experiencing an issue with the `unist-util-visit` library where node type checking is not working as expected. When traversing a tree and filtering by node type, nodes that don't match the specified type are still being processed.

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
  console.log(node.type)
  // Expected: only logs 'paragraph'
  // Actual: logs both 'paragraph' and 'heading'
})
```

### Expected behavior

The visitor function should only be called for nodes that match the specified type. In the example above, only the paragraph node should be visited, but it seems like the type filter isn't working correctly.

### Additional context

This seems to have started recently. The type checking logic appears to be broken - nodes are being visited regardless of their type when a specific type filter is provided.

---
Repository: /testbed
