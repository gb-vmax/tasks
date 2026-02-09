# Bug Report

### Describe the bug

I'm experiencing an issue with the `visit` function in the unist-util-remove-position vendor code. When visiting nodes in a tree structure, the visitor callback receives incorrect parent information - it seems to be getting the grandparent node instead of the actual parent node.

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
};

visit(tree, (node, index, parent) => {
  if (node.type === 'text') {
    console.log('Parent type:', parent.type);
    // Expected: 'paragraph'
    // Actual: 'root' (or undefined in some cases)
  }
});
```

### Expected behavior

The `parent` parameter passed to the visitor callback should reference the immediate parent node of the current node being visited. For a text node inside a paragraph, the parent should be the paragraph node, not the root node.

### Additional context

This also affects the `index` parameter since it's calculated based on the wrong parent node. The index becomes incorrect or undefined when it should be a valid position in the parent's children array.

---
Repository: /testbed
