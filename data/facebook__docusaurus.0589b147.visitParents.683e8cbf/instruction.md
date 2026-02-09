# Bug Report

### Describe the bug

When traversing AST nodes in non-reverse order (forward traversal), child nodes are being skipped and not visited properly. The tree visitor appears to be moving in the wrong direction during forward iteration.

### Reproduction

```js
const tree = {
  type: 'root',
  children: [
    { type: 'paragraph', children: [{ type: 'text', value: 'first' }] },
    { type: 'paragraph', children: [{ type: 'text', value: 'second' }] },
    { type: 'paragraph', children: [{ type: 'text', value: 'third' }] }
  ]
}

const visited = []
visitParents(tree, 'text', (node) => {
  visited.push(node.value)
})

// Expected: ['first', 'second', 'third']
// Actual: only 'first' is visited, remaining nodes are skipped
```

### Expected behavior

All child nodes should be visited in forward order when `reverse` is not set or is `false`. The visitor should traverse through all children sequentially from index 0 to length-1.

### System Info

- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
