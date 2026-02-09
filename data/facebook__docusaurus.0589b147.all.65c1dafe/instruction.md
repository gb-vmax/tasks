# Bug Report

### Describe the bug

I'm experiencing an issue with markdown processing where the first element in a collection is being skipped. When processing multiple markdown nodes, the output is missing the content from the first node in the sequence.

### Reproduction

```js
// Processing a list of markdown nodes
const nodes = [
  { type: 'text', value: 'First item' },
  { type: 'text', value: 'Second item' },
  { type: 'text', value: 'Third item' }
]

// Expected output: "First itemSecond itemThird item"
// Actual output: "Second itemThird item"
```

The first element is consistently being dropped from the output. This seems to affect any collection of nodes being processed together.

### Expected behavior

All nodes in a collection should be processed and included in the output, including the first one. The current behavior skips the initial element which breaks content rendering.

### System Info
- remark version: 15.0.1
- Node version: Latest

---
Repository: /testbed
