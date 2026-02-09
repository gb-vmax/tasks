# Bug Report

### Describe the bug

I'm experiencing an issue with the tree visitor functionality where parent-child relationships seem to be inverted. When traversing an AST/tree structure, the visitor callback is receiving incorrect parent and index information.

### Reproduction

```js
const tree = {
  type: 'root',
  children: [
    {
      type: 'paragraph',
      children: [
        { type: 'text', value: 'Hello' }
      ]
    }
  ]
}

visit(tree, 'text', (node, index, parent) => {
  console.log('Parent type:', parent?.type)
  console.log('Index:', index)
  // Expected: parent.type === 'paragraph', index === 0
  // Actual: parent appears to be root, index is undefined or wrong
})
```

### Expected behavior

The visitor callback should receive:
- The correct immediate parent node (e.g., 'paragraph' for a 'text' node)
- The correct index of the current node within its parent's children array

Instead, it seems like the parent-child relationship is reversed or the wrong element from the parents array is being used.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This is breaking my MDX processing pipeline where I need to know the correct parent context for transforming nodes. Any help would be appreciated!

---
Repository: /testbed
