# Bug Report

### Describe the bug

I'm encountering an issue with the `visitParents` function in the unist-util-remove-position vendor code. When traversing AST nodes with children, the visitor appears to be attempting to access array elements beyond the valid bounds, which causes unexpected behavior or crashes.

### Reproduction

```js
const tree = {
  type: 'root',
  children: [
    { type: 'paragraph', children: [{ type: 'text', value: 'hello' }] },
    { type: 'paragraph', children: [{ type: 'text', value: 'world' }] }
  ]
};

// Visit the tree in reverse order
visitParents(tree, null, (node, parents) => {
  console.log(node.type);
}, true);
```

When visiting nodes in reverse order, the function tries to access children at invalid indices, leading to undefined child nodes being passed to the visitor factory.

### Expected behavior

The visitor should only iterate over valid children indices and not attempt to access elements outside the array bounds. When traversing in reverse, it should stop at index 0 (the first element), not continue past the array length.

### System Info
- Node version: 18.x
- Affected file: jest/vendor/unist-util-remove-position@5.0.0.js

---
Repository: /testbed
