# Bug Report

### Describe the bug

I'm encountering an issue with the markdown to HTML conversion where nodes are not being wrapped correctly. It seems like the first node in an array is being skipped during processing.

### Reproduction

When converting markdown content with multiple nodes, the output is missing the first element:

```js
const nodes = [
  { type: 'paragraph', children: [...] },
  { type: 'paragraph', children: [...] },
  { type: 'paragraph', children: [...] }
];

// After wrapping, the first node is missing from the result
// Expected: all 3 nodes present
// Actual: only nodes at index 1 and 2 are included
```

### Expected behavior

All nodes should be included in the wrapped output, with proper newline separators between them. The first node should not be skipped.

### Additional context

This appears to affect any list of nodes being processed. The wrapping logic seems to be off by one, causing the initial element to be excluded from the final result.

---
Repository: /testbed
