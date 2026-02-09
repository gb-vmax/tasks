# Bug Report

### Describe the bug

I'm encountering an issue with tree traversal when using `visitParents` in reverse mode. When traversing a tree structure with the `reverse` parameter set to `true`, the function appears to hang or loop indefinitely instead of properly iterating through the children in reverse order.

### Reproduction

```js
const tree = {
  type: 'root',
  children: [
    { type: 'paragraph', children: [{ type: 'text', value: 'first' }] },
    { type: 'paragraph', children: [{ type: 'text', value: 'second' }] },
    { type: 'paragraph', children: [{ type: 'text', value: 'third' }] }
  ]
};

visitParents(tree, 'paragraph', (node, ancestors) => {
  console.log(node);
}, true); // reverse = true

// Expected: visits paragraphs in reverse order (third, second, first)
// Actual: hangs/infinite loop
```

### Expected behavior

When `reverse` is set to `true`, the visitor should traverse the tree's children in reverse order, starting from the last child and moving towards the first. The traversal should complete successfully without hanging.

### Additional context

This seems to work fine when `reverse` is `false` or not specified. The issue only occurs when explicitly setting `reverse: true`.

---
Repository: /testbed
