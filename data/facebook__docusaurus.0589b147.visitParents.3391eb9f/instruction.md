# Bug Report

### Describe the bug

I'm experiencing an issue with tree traversal when using the `SKIP` action in the visitor function. When I return `SKIP` from a visitor, the traversal seems to be skipping nodes incorrectly - it's visiting children when it should skip them, and the offset calculation appears wrong.

### Reproduction

```js
const tree = {
  type: 'root',
  children: [
    {
      type: 'parent',
      children: [
        { type: 'leaf', value: 'a' },
        { type: 'leaf', value: 'b' }
      ]
    },
    { type: 'leaf', value: 'c' }
  ]
};

visitParents(tree, 'parent', (node) => {
  // Returning SKIP should skip visiting the children of this node
  return [SKIP];
});

// Expected: Children of 'parent' node should not be visited
// Actual: Children are being visited anyway
```

### Expected behavior

When returning `SKIP` from the visitor function, the traversal should skip visiting the children of that node and move to the next sibling. The current behavior seems inverted - it's processing children when `SKIP` is returned instead of skipping them.

### System Info
- Version: Latest from main branch
- The issue appears to be in the `visitParents` function logic

---
Repository: /testbed
