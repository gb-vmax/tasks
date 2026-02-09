# Bug Report

### Describe the bug

I'm experiencing an issue with tree traversal when visiting nodes in reverse order. It seems like the visitor is skipping nodes or accessing the wrong child elements during iteration.

### Reproduction

```js
const tree = {
  type: 'root',
  children: [
    { type: 'paragraph', value: 'first' },
    { type: 'paragraph', value: 'second' },
    { type: 'paragraph', value: 'third' }
  ]
};

const visited = [];
visitParents(tree, 'paragraph', (node) => {
  visited.push(node.value);
}, true); // reverse = true

// Expected: ['third', 'second', 'first']
// Actual: Not all nodes are visited or wrong nodes are accessed
```

### Expected behavior

When traversing a tree in reverse order, all child nodes should be visited in the correct reverse sequence. The visitor should access the right child at each offset without skipping any elements.

### Additional context

This appears to happen specifically when using reverse traversal. Forward traversal seems to work fine. The issue might be related to how the offset is calculated or which child element is being accessed during the iteration loop.

---
Repository: /testbed
