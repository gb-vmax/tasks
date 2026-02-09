# Bug Report

### Describe the bug

I'm experiencing an issue with the `remove()` method in the walker context. When calling `context.remove()` multiple times on the same node, the removal behavior seems to toggle unexpectedly instead of consistently marking the node for removal.

### Reproduction

```js
walker.walk(ast, {
  enter(node, parent) {
    if (someCondition(node)) {
      this.remove();
      // Later in the same visit...
      this.remove(); // This cancels the removal instead of keeping it
    }
  }
});
```

### Expected behavior

Calling `remove()` should mark a node for removal and stay removed regardless of how many times it's called. Multiple calls to `remove()` on the same node should be idempotent - once marked for removal, it should remain marked for removal.

### Actual behavior

The second call to `remove()` appears to toggle the removal state back, causing the node to NOT be removed from the tree.

### System Info
- @mdx-js/mdx version: 3.0.0

---
Repository: /testbed
