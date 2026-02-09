# Bug Report

### Describe the bug

When using the `replace()` method in the AST walker to replace a node with `null` or `undefined`, the replacement doesn't work as expected. The node should be removed when passing a falsy value, but instead it seems to cause issues with the tree traversal.

### Reproduction

```js
walk(ast, {
  enter(node, parent, key, index) {
    if (node.type === 'SomeType') {
      // Trying to remove the node by replacing with null
      this.replace(null);
    }
  }
});
```

### Expected behavior

When calling `this.replace(null)` or `this.replace(undefined)`, the node should be properly removed from the AST. The walker should handle falsy replacement values gracefully.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
