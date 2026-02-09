# Bug Report

### Describe the bug

I'm experiencing an issue with tree traversal where nodes are being skipped when they shouldn't be. It seems like the visitor function is not being called on nodes that match the test condition.

### Reproduction

```js
const tree = {
  type: 'root',
  children: [
    { type: 'paragraph', children: [] },
    { type: 'heading', children: [] }
  ]
};

// Visit all paragraph nodes
visitParents(tree, 'paragraph', (node) => {
  console.log('Visiting:', node.type);
});

// Expected: Should log "Visiting: paragraph"
// Actual: Nothing is logged
```

When I specify a test condition to match certain node types, the visitor callback is never invoked even though matching nodes exist in the tree. If I remove the test parameter and visit all nodes, it works fine.

### Expected behavior

The visitor function should be called for all nodes that match the test condition. In the example above, it should visit the paragraph node and log its type.

### System Info
- Node version: 18.x
- Using remark-rehype 11.0.0

---
Repository: /testbed
