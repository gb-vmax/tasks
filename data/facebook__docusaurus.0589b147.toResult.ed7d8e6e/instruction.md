# Bug Report

### Describe the bug

I'm experiencing an issue with tree traversal when using visitor functions that return arrays. It seems like when a visitor function returns an array with multiple values (like `[action, index]`), only the first element is being processed instead of the full array.

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

visit(tree, 'paragraph', (node, index) => {
  // Returning an array with action and index
  return [SKIP, index + 1]
})
```

### Expected behavior

When the visitor returns an array like `[SKIP, 2]`, both the action (SKIP) and the index (2) should be used to control the traversal. The function should skip the current node and continue from index 2.

### Actual behavior

Only the first element of the returned array is being used, so the index parameter is being ignored. This breaks the ability to control which node to visit next.

This is affecting tree manipulation workflows where I need to skip certain nodes and jump to specific positions in the tree.

---
Repository: /testbed
