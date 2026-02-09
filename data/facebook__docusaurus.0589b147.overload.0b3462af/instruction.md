# Bug Report

### Describe the bug

I'm experiencing an issue with the `visit` function where parent node information is being passed incorrectly to the visitor callback. The parent node that's being provided doesn't match the actual parent of the current node being visited.

### Reproduction

```js
const tree = {
  type: 'root',
  children: [
    {
      type: 'paragraph',
      children: [
        { type: 'text', value: 'hello' }
      ]
    }
  ]
}

visit(tree, 'text', (node, index, parent) => {
  console.log('Node:', node.value)
  console.log('Parent type:', parent.type)
  console.log('Index:', index)
  // Expected: parent should be 'paragraph', but getting 'root' instead
  // Expected: index should be 0, but getting undefined
})
```

### Expected behavior

When visiting a deeply nested node, the `parent` parameter should be the immediate parent of that node, and `index` should be the position of the node within that parent's children array. For example, when visiting a text node inside a paragraph, the parent should be the paragraph node, not the root.

### Additional context

This seems to affect tree traversal operations where you need accurate parent/child relationships, like when trying to modify or remove nodes based on their context.

---
Repository: /testbed
