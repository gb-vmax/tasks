# Bug Report

### Describe the bug

I'm experiencing an issue with tree traversal where nodes that should be visited are being skipped. It appears that the visitor function is not being called for nodes that match the test condition.

### Reproduction

```js
const tree = {
  type: 'root',
  children: [
    { type: 'paragraph', children: [] },
    { type: 'heading', children: [] }
  ]
};

let visited = [];
visit(tree, 'paragraph', (node) => {
  visited.push(node.type);
});

// Expected: visited = ['paragraph']
// Actual: visited = []
```

When I specify a test condition to filter which nodes to visit, the visitor function never gets called even though matching nodes exist in the tree. If I remove the test parameter and visit all nodes, it works as expected.

### Expected behavior

The visitor function should be called for all nodes that match the test condition. In the example above, the paragraph node should be visited and added to the array.

### Additional context

This seems to have started happening recently. The behavior is inverted - nodes that match the condition are being skipped instead of visited.

---
Repository: /testbed
