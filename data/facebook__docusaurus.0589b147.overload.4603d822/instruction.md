# Bug Report

### Describe the bug

I'm experiencing an issue with the tree visitor where the parent node being passed to the visitor callback appears to be incorrect. When traversing a tree structure, the parent parameter seems to be pointing to the wrong node in the hierarchy.

### Reproduction

```js
const tree = {
  type: 'root',
  children: [
    {
      type: 'parent',
      children: [
        { type: 'child', value: 'test' }
      ]
    }
  ]
}

visit(tree, 'child', (node, index, parent) => {
  console.log('Parent type:', parent.type)
  // Expected: 'parent'
  // Actual: 'root'
})
```

### Expected behavior

The `parent` parameter in the visitor callback should reference the immediate parent of the current node. In the example above, when visiting a node of type 'child', the parent should be the 'parent' node, not the 'root' node.

### Additional context

This seems to affect the entire tree traversal mechanism. The parent being passed is one level higher in the tree than it should be, which breaks any logic that depends on getting the correct parent reference.

---
Repository: /testbed
