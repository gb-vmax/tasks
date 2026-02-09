# Bug Report

### Describe the bug

I'm experiencing an issue with tree traversal when using `visitParents` on nested node structures. The visitor function seems to stop prematurely and doesn't visit all child nodes in the tree.

### Reproduction

```js
const tree = {
  type: 'root',
  children: [
    {
      type: 'parent',
      children: [
        { type: 'leaf', value: 'first' },
        { type: 'leaf', value: 'second' }
      ]
    },
    {
      type: 'parent',
      children: [
        { type: 'leaf', value: 'third' }
      ]
    }
  ]
};

const visited = [];
visitParents(tree, (node) => {
  visited.push(node.type);
});

// Expected: ['root', 'parent', 'leaf', 'leaf', 'parent', 'leaf']
// Actual: Only visits the first few nodes before stopping
```

The traversal stops early and doesn't complete visiting all nodes in the tree. It seems like the visitor exits prematurely when processing child nodes, even though it should continue traversing the entire tree structure.

### Expected behavior

The `visitParents` function should traverse the entire tree and visit all nodes, including deeply nested children. The traversal should only stop if explicitly instructed to do so (e.g., returning EXIT from the visitor).

### System Info
- unist-util-remove-position version: 5.0.0
- Node.js version: Latest

---
Repository: /testbed
