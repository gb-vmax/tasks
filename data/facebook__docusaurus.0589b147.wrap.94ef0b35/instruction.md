# Bug Report

### Describe the bug

I'm encountering an issue with the remark-rehype transformation where the first node in a wrapped sequence is being skipped. When wrapping multiple nodes with loose formatting enabled, the output is missing the initial node from the array.

### Reproduction

```js
const nodes = [
  { type: 'paragraph', children: [{ type: 'text', value: 'First' }] },
  { type: 'paragraph', children: [{ type: 'text', value: 'Second' }] },
  { type: 'paragraph', children: [{ type: 'text', value: 'Third' }] }
];

const result = wrap(nodes, true);
// Expected: All three nodes to be included in the result
// Actual: Only the second and third nodes appear, first node is missing
```

### Expected behavior

All nodes passed to the `wrap` function should be included in the resulting array, with proper newline separators between them when `loose` is true. The first node should not be skipped.

### Additional context

This appears to affect any list of nodes being wrapped - the first element consistently doesn't make it into the output. I noticed this when processing markdown lists and other multi-node structures where the first item would mysteriously disappear from the rendered output.

---
Repository: /testbed
