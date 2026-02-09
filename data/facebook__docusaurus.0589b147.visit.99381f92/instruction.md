# Bug Report

### Describe the bug

I'm experiencing an issue with the tree visitor utility where the parent node being passed to the visitor function appears to be incorrect. When traversing nested tree structures, the visitor callback receives what seems to be the root node instead of the immediate parent node.

### Reproduction

```js
const tree = {
  type: 'root',
  children: [
    {
      type: 'parent',
      children: [
        {
          type: 'child',
          value: 'test'
        }
      ]
    }
  ]
}

visit(tree, (node, index, parent) => {
  if (node.type === 'child') {
    console.log('Parent type:', parent.type)
    // Expected: 'parent'
    // Actual: 'root'
  }
})
```

### Expected behavior

The visitor function should receive the immediate parent node, not the root or some other ancestor. In the example above, when visiting a 'child' node, the parent parameter should be the 'parent' node, not the 'root' node.

This is breaking my use case where I need to access sibling nodes through the parent's children array.

### Additional context

This seems to have started recently. The tree traversal itself works fine, but the parent reference passed to the callback is wrong for deeply nested nodes.

---
Repository: /testbed
