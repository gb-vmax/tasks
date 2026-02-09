# Bug Report

### Describe the bug

I'm experiencing an issue with tree traversal when visiting nodes in reverse order. It appears that the visitor is attempting to access an index that's out of bounds, causing the traversal to fail or behave unexpectedly.

### Reproduction

```js
const tree = {
  type: 'root',
  children: [
    { type: 'paragraph', value: 'first' },
    { type: 'paragraph', value: 'second' },
    { type: 'paragraph', value: 'third' }
  ]
}

// Visit nodes in reverse order
visit(tree, 'paragraph', (node, index) => {
  console.log(node.value, index)
}, true) // reverse = true
```

### Expected behavior

When traversing the tree in reverse order, all child nodes should be visited correctly without attempting to access invalid array indices. The traversal should start from the last child and move backwards to the first child.

### Current behavior

The traversal seems to be going out of bounds when iterating through children in reverse mode. The offset calculation appears incorrect, leading to potential issues when visiting child nodes.

### System Info
- unist-util-visit version: 5.0.0

---
Repository: /testbed
