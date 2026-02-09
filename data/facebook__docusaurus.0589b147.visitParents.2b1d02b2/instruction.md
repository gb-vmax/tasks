# Bug Report

### Describe the bug
When traversing trees in reverse order, the visitor function appears to be exiting prematurely instead of continuing to visit all nodes. The tree traversal stops unexpectedly early when processing nodes in reverse.

### Reproduction
```js
const tree = {
  type: 'root',
  children: [
    { type: 'node1' },
    { type: 'node2' },
    { type: 'node3' }
  ]
};

// Traverse in reverse order
visitParents(tree, null, (node) => {
  console.log(node.type);
  return CONTINUE;
}, true);

// Expected: logs 'node3', 'node2', 'node1', 'root'
// Actual: only logs 'root' or stops after first node
```

### Expected behavior
When traversing in reverse mode, all child nodes should be visited starting from the last child and moving backwards. The visitor should process each node unless explicitly told to skip or exit.

### Additional context
This seems to affect reverse tree traversal specifically. Forward traversal appears to work as expected. The issue manifests when trying to process tree structures from bottom to top or right to left.

---
Repository: /testbed
