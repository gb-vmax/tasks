# Bug Report

### Describe the bug

I'm experiencing an issue with the remark parser where node type checking seems to be inverted. When I try to filter or validate nodes by their type, I'm getting the opposite results - nodes that should match are being excluded, and nodes that shouldn't match are being included.

### Reproduction

```js
// Trying to filter for 'heading' nodes
const headings = tree.children.filter(typeFactory('heading'));

// Expected: only heading nodes
// Actual: everything EXCEPT heading nodes
```

This is breaking my markdown processing pipeline as none of the type-based filters are working correctly anymore.

### Expected behavior

When using `typeFactory` to check node types, it should return `true` for nodes that match the specified type and `false` for nodes that don't match. Currently it appears to be doing the inverse.

### Additional context

This seems to have started recently. My code that was working before is now filtering out all the nodes I actually want to keep. It's like the type checking logic got flipped somehow.

---
Repository: /testbed
