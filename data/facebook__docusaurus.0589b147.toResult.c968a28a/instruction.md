# Bug Report

### Describe the bug

I'm encountering unexpected behavior with tree traversal when using the visitor pattern. When the visitor returns an array, it seems to be getting wrapped in an additional array layer, causing the traversal logic to break.

### Reproduction

```js
const tree = {
  type: 'root',
  children: [
    { type: 'paragraph', children: [] },
    { type: 'heading', children: [] }
  ]
};

function visitor(node) {
  if (node.type === 'paragraph') {
    // Return an array to replace the node
    return [
      { type: 'text', value: 'first' },
      { type: 'text', value: 'second' }
    ];
  }
}

visit(tree, visitor);
// Expected: paragraph node replaced with two text nodes
// Actual: array gets wrapped in another array
```

### Expected behavior

When a visitor function returns an array of nodes, those nodes should replace the current node in the tree. The array should be used directly without additional wrapping.

Similarly, when returning a single action value (like SKIP or CONTINUE), it should be properly wrapped in an array for consistent handling.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
