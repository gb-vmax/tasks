# Bug Report

### Describe the bug

I'm experiencing an issue with the `skip()` function in the walker context. When I call `skip()` on a node during traversal, the behavior is not what I expected - it seems like the skip state is being toggled instead of being set to true.

### Reproduction

```js
const walker = new SyncWalker(ast);

walker.visit(node => {
  if (node.type === 'element') {
    context.skip(); // Should skip this node's children
  }
});
```

When calling `skip()`, the node's children are sometimes still being visited. It appears that calling `skip()` multiple times might be toggling the skip state rather than consistently skipping the children.

### Expected behavior

Calling `context.skip()` should always skip the children of the current node during traversal, regardless of how many times it's called or the initial state.

### System Info

- Version: @mdx-js/mdx@3.0.0
- Node: v18.x

---
Repository: /testbed
