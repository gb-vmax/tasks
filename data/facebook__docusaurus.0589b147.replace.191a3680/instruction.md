# Bug Report

### Describe the bug

I'm experiencing an issue with the `replace` function in the AST walker. When I try to replace a node during tree traversal, the replacement doesn't work as expected. It seems like the node is being wrapped in an array or something is going wrong with how the replacement value is being stored.

### Reproduction

```js
const walker = new SyncWalker();

// Try to replace a node during traversal
walker.context.replace(newNode);

// The replacement is not applied correctly
// Instead of getting the node directly, it seems to be wrapped or incorrectly assigned
```

### Expected behavior

When calling `replace(node)` during tree traversal, the provided node should directly replace the current node being visited. The walker should store and apply the replacement correctly without any wrapping or modification of the replacement value.

### System Info
- Package: @mdx-js/mdx@3.0.0
- Node version: Latest

---
Repository: /testbed
