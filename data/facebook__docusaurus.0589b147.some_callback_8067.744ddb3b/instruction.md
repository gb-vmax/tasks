# Bug Report

### Describe the bug

I'm experiencing an issue with markdown rendering where documents that contain only phrasing content (inline elements like text, emphasis, links, etc.) are being incorrectly processed as flow content (block-level elements).

### Reproduction

```js
const ast = {
  type: 'root',
  children: [
    { type: 'text', value: 'Hello ' },
    { type: 'emphasis', children: [{ type: 'text', value: 'world' }] },
    { type: 'text', value: '!' }
  ]
};

// The root should be treated as phrasing content since all children are phrasing nodes
// But it's being processed as flow content instead
```

### Expected behavior

When a root node contains only phrasing content (inline elements), it should be handled with `containerPhrasing` instead of `containerFlow`. Currently, documents with purely inline content are being treated as if they contain block-level elements, which affects the output formatting.

### System Info
- remark version: 15.0.1
- Node.js version: 18.x

---
Repository: /testbed
