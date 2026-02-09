# Bug Report

### Describe the bug

I'm encountering an issue with tree traversal in the `unist-util-remove-position` vendor module. When traversing a tree structure in reverse order, the traversal doesn't start from the correct position and appears to be skipping elements or starting from an incorrect index.

### Reproduction

```js
const tree = {
  type: 'root',
  children: [
    { type: 'node1', value: 'first' },
    { type: 'node2', value: 'second' },
    { type: 'node3', value: 'third' }
  ]
};

// When visiting in reverse order
visitParents(tree, null, (node) => {
  console.log(node.value);
}, true);

// Expected: 'third', 'second', 'first'
// Actual: incorrect traversal order or missing nodes
```

### Expected behavior

When `reverse` is set to `true`, the tree should be traversed starting from the last child and moving backwards through all children. The offset calculation should correctly position at the last element when traversing in reverse.

### Additional context

This seems to affect how the initial offset is calculated when starting a reverse traversal. The traversal either starts at the wrong position or doesn't visit all nodes as expected.

---
Repository: /testbed
