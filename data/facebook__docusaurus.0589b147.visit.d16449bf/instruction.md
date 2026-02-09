# Bug Report

### Describe the bug
I'm experiencing an issue with tree traversal when using the `visit` function. When visiting nodes in a tree structure, the visitor function receives incorrect index values for nodes that appear multiple times as children of the same parent.

### Reproduction
```js
const tree = {
  type: 'root',
  children: [
    { type: 'paragraph', value: 'first' },
    { type: 'paragraph', value: 'second' },
    { type: 'paragraph', value: 'third' }
  ]
}

visit(tree, (node, index, parent) => {
  if (node.type === 'paragraph') {
    console.log(`Node at index: ${index}`)
    // Expected: 0, 1, 2
    // Actual: wrong index values
  }
})
```

The index parameter passed to the visitor callback doesn't match the actual position of the node in the parent's children array. This breaks any logic that relies on knowing the correct position of a node.

### Expected behavior
The visitor callback should receive the correct index of the current node within its parent's children array. For sequential children, this should be 0, 1, 2, etc.

### Additional context
This seems to affect any code that needs to:
- Insert nodes at specific positions
- Remove nodes based on their index
- Reorder children based on their positions

The issue appears to be related to how node indices are determined during traversal.

---
Repository: /testbed
