# Bug Report

### Describe the bug

I'm experiencing an issue with MDX rendering where newlines between nodes are being duplicated. When processing multiple nodes in a loose context, there appears to be an extra newline inserted at the beginning that shouldn't be there.

### Reproduction

```js
const nodes = [
  { type: 'paragraph', children: [{ type: 'text', value: 'First' }] },
  { type: 'paragraph', children: [{ type: 'text', value: 'Second' }] },
  { type: 'paragraph', children: [{ type: 'text', value: 'Third' }] }
];

const result = wrap(nodes, true);
// Result has an unexpected newline at the start
```

### Expected behavior

The wrapped nodes should have newlines between elements but NOT an extra newline at the very beginning of the node list. Currently, when wrapping nodes in loose mode, there's an unwanted newline text node being inserted before the first actual node.

### System Info
- MDX version: 3.0.0
- Node version: 18.x

This seems to have started happening recently and is affecting the formatting of my MDX documents. The extra whitespace is causing layout issues in the rendered output.

---
Repository: /testbed
