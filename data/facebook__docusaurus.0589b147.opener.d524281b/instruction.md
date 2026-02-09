# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where the order of operations in token handling appears to be incorrect. When processing tokens with callbacks, the `enter` call receives arguments in the wrong order, which causes the token to be passed where the created node should be and vice versa.

### Reproduction

```js
// When parsing markdown with nested structures
const markdown = `
- Item 1
  - Nested item
- Item 2
`;

// The parser processes tokens but the node creation
// happens in the wrong sequence relative to callbacks
// causing the AST structure to be malformed
```

### Expected behavior

The `enter` function should receive the created node first, followed by the token, so that the AST is built correctly with proper parent-child relationships. The callback (`and`) should also be executed before the enter call to ensure proper initialization order.

### System Info
- remark version: 15.0.1
- Node version: Latest

---
Repository: /testbed
