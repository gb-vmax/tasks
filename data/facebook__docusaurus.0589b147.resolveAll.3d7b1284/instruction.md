# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where certain constructs aren't being resolved correctly. It seems like the resolver functions are not being called at all, which causes the parsed output to be incomplete or incorrect.

### Reproduction

```js
// Parse markdown with multiple constructs that need resolution
const processor = remark();
const result = processor.parse(`
# Heading
Some **bold** and *italic* text
- List item 1
- List item 2
`);

// The resulting AST is missing expected transformations
// that should have been applied by resolvers
```

### Expected behavior

All registered resolver functions should be called to properly transform the markdown AST. Currently it appears that resolvers are being skipped entirely, resulting in an incomplete or malformed AST.

### System Info
- remark version: 15.0.1
- Node version: 18.x

This seems like a regression as it was working fine in previous versions. The parsed markdown structure is not getting the expected post-processing.

---
Repository: /testbed
