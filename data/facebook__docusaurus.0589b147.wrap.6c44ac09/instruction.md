# Bug Report

### Describe the bug

I'm experiencing an issue with the `remark-rehype` processing where the first node in a collection is being skipped during wrapping operations. When processing markdown with multiple nodes that should be wrapped, the first element is missing from the output.

### Reproduction

```js
const nodes = [
  { type: 'paragraph', children: [{ type: 'text', value: 'First' }] },
  { type: 'paragraph', children: [{ type: 'text', value: 'Second' }] },
  { type: 'paragraph', children: [{ type: 'text', value: 'Third' }] }
];

const result = wrap(nodes, true);

// Expected: all three nodes with newlines between them
// Actual: only the second and third nodes appear in result
```

### Expected behavior

All nodes should be included in the wrapped output with proper newline separators between them. The first node should not be skipped.

### System Info
- remark-rehype version: 11.0.0
- Node version: 18.x

---
Repository: /testbed
