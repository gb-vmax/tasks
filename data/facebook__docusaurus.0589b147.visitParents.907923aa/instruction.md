# Bug Report

### Describe the bug

I'm experiencing an issue with tree traversal when using the unist utility functions. When traversing a tree in reverse order, the visitor function seems to be starting from the wrong index, causing some nodes to be skipped or visited incorrectly.

### Reproduction

```js
const tree = {
  type: 'root',
  children: [
    { type: 'node', value: 'first' },
    { type: 'node', value: 'second' },
    { type: 'node', value: 'third' }
  ]
};

// Traverse in reverse
visitParents(tree, 'node', (node, index, parents) => {
  console.log(node.value, index);
}, true);

// Expected output: third 2, second 1, first 0
// Actual output: Nodes are not visited in correct order or some are skipped
```

### Expected behavior

When traversing a tree in reverse order, all child nodes should be visited starting from the last child (highest index) down to the first child (index 0). The offset calculation should properly initialize to the last valid index when reverse is true.

Additionally, when building the grandparents array for nested traversal, the correct node reference should be passed to maintain the proper parent chain.

### System Info
- unist-util-remove-position version: 5.0.0
- Node version: 18.x

---
Repository: /testbed
