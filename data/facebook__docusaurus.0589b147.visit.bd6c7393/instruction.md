# Bug Report

### Describe the bug

I'm experiencing an issue with the `visit` function where the parent node and index being passed to the visitor callback appear to be incorrect. When traversing a tree structure, the visitor receives what seems to be the grandparent node instead of the actual parent, and the index doesn't match the expected position of the current node in its parent's children array.

### Reproduction

```js
const tree = {
  type: 'root',
  children: [
    {
      type: 'parent',
      children: [
        { type: 'leaf', value: 'test' }
      ]
    }
  ]
};

visit(tree, 'leaf', (node, index, parent) => {
  console.log('Node:', node.type);
  console.log('Parent:', parent?.type);
  console.log('Index:', index);
  // Expected: parent.type = 'parent', index = 0
  // Actual: parent.type = 'root', index = -1 or incorrect
});
```

### Expected behavior

The visitor callback should receive:
- The current node
- The correct index of the node within its parent's children array
- The direct parent node (not the grandparent)

Instead, it seems like the parent is shifted up one level in the tree hierarchy, causing incorrect parent references and index calculations.

### System Info
- unist-util-visit version: 5.0.0

---
Repository: /testbed
