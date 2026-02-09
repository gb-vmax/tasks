# Bug Report

### Describe the bug

I'm experiencing an issue with the tree visitor function where the parent node being passed to the visitor callback is incorrect. When traversing a tree structure, the visitor receives the wrong parent node - it seems to be getting the grandparent instead of the actual parent.

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

visit(tree, (node, index, parent) => {
  if (node.type === 'text') {
    console.log('Parent type:', parent.type)
    // Expected: 'paragraph'
    // Actual: 'root'
  }
})
```

### Expected behavior

When visiting a text node, the parent parameter should be the immediate parent (the paragraph node), not the grandparent (the root node). The index should also correctly reflect the position within the actual parent's children array.

### Additional context

This seems to have broken recently and is causing issues when trying to manipulate nodes based on their parent context. The visitor callback signature is supposed to be `(node, index, parent)` where parent is the direct parent of the current node.

---
Repository: /testbed
