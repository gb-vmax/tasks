# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where certain constructs are not being resolved correctly. It seems like some resolver functions are being skipped or called multiple times when they shouldn't be.

### Reproduction

```js
// Parse markdown with multiple constructs that have resolvers
const processor = remark();
const result = processor.parse(`
# Heading
Some text with **bold** and *italic*
- list item 1
- list item 2
`);

// The resulting AST has incorrect structure
// Some nodes are not properly resolved
```

### Expected behavior

All construct resolvers should be called exactly once in the correct order, and the resulting AST should have all nodes properly resolved with correct relationships between parent and child nodes.

### Additional context

This appears to affect documents with multiple types of constructs that have `resolveAll` functions. The parsing completes without errors but the output structure is incorrect.

---
Repository: /testbed
