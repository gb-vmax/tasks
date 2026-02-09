# Bug Report

### Describe the bug

I'm experiencing an issue with tree traversal where the parent node and index information passed to visitor functions appears to be incorrect. When visiting nodes in a tree structure, the visitor callback receives the wrong parent node (seems to be skipping one level up) and the index calculation is also off.

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
}

visit(tree, 'leaf', (node, index, parent) => {
  console.log('Parent type:', parent.type)  // Expected: 'parent', Actual: 'root'
  console.log('Index:', index)               // Index is also incorrect
})
```

### Expected behavior

The visitor function should receive:
- The immediate parent of the current node (not a grandparent)
- The correct index of the node within its parent's children array

This is causing issues when trying to manipulate or analyze the tree structure, as I can't reliably determine the node's position or access its direct parent.

### System Info
- unist-util-visit version: 5.0.0

---
Repository: /testbed
