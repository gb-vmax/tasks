# Bug Report

### Describe the bug

I'm experiencing an issue with tree traversal in the unist-util-remove-position utility. When using the visitor pattern to traverse a syntax tree, child nodes are being visited even when the parent node returns a SKIP action. This causes the traversal to continue into subtrees that should be skipped.

### Reproduction

```js
const tree = {
  type: 'root',
  children: [
    {
      type: 'parent',
      children: [
        { type: 'child1' },
        { type: 'child2' }
      ]
    }
  ]
};

visitParents(tree, (node) => {
  if (node.type === 'parent') {
    // Returning SKIP should prevent visiting child1 and child2
    return SKIP;
  }
  console.log('Visited:', node.type);
});

// Expected: Only 'root' and 'parent' are logged
// Actual: 'root', 'parent', 'child1', and 'child2' are all logged
```

### Expected behavior

When a visitor function returns `SKIP` for a node, the traversal should skip visiting that node's children and continue with the next sibling. The children of the skipped node should not be processed.

### System Info
- Version: 5.0.0
- Environment: Jest vendor bundle

---
Repository: /testbed
