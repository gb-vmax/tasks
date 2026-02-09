# Bug Report

### Describe the bug

I'm encountering an issue with the AST walker's `replace` function. When I try to replace a node in the tree, the replacement doesn't actually happen and the original node remains in place.

### Reproduction

```js
const walker = new SyncWalker(ast, {
  enter(node, parent) {
    if (node.type === 'Paragraph') {
      this.replace(newNode);
    }
  }
});

walker.walk();
// The paragraph node is not replaced with newNode
```

### Expected behavior

When calling `this.replace(newNode)` in the walker's enter/leave callbacks, the current node should be replaced with the provided node in the AST.

### Additional context

This seems to have broken recently. The replace function is being called but the node replacement isn't taking effect. The AST remains unchanged after walking through it.

---
Repository: /testbed
