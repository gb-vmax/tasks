# Bug Report

### Describe the bug

When processing MDX content with multiple nodes, the last node in the array is being dropped during the wrap operation. This causes content to be missing from the rendered output.

### Reproduction

```js
const nodes = [
  { type: "paragraph", children: [{ type: "text", value: "First" }] },
  { type: "paragraph", children: [{ type: "text", value: "Second" }] },
  { type: "paragraph", children: [{ type: "text", value: "Third" }] }
];

const result = wrap(nodes, false);
// Expected: all 3 nodes
// Actual: only first 2 nodes are included
```

The third node is missing from the result. This happens when wrapping nodes without loose mode.

### Expected behavior

All nodes in the input array should be included in the wrapped result, regardless of the loose parameter value.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
