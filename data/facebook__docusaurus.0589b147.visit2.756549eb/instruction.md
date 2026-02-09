# Bug Report

### Describe the bug

When using `visitParents` with `reverse: true` option, the tree traversal doesn't work correctly. The visitor function doesn't visit all nodes in reverse order as expected, and some nodes appear to be skipped entirely.

### Reproduction

```js
const tree = {
  type: 'root',
  children: [
    { type: 'paragraph', children: [{ type: 'text', value: 'first' }] },
    { type: 'paragraph', children: [{ type: 'text', value: 'second' }] },
    { type: 'paragraph', children: [{ type: 'text', value: 'third' }] }
  ]
};

const visited = [];
visitParents(tree, (node) => {
  visited.push(node.type);
}, true); // reverse = true

// Expected: nodes visited in reverse order
// Actual: some nodes not visited or visited in wrong order
```

### Expected behavior

When `reverse` is set to `true`, the tree should be traversed in reverse order, visiting all child nodes from last to first. All nodes should still be visited.

### System Info
- unist-util-visit version: 5.0.0

---
Repository: /testbed
