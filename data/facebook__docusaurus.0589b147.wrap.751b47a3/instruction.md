# Bug Report

### Describe the bug

I'm experiencing an issue with MDX rendering where an extra newline appears to be added at the end of wrapped node lists. This seems to be causing unexpected formatting in the output.

### Reproduction

When processing MDX content with multiple nodes that need to be wrapped, the output includes an additional newline character that shouldn't be there. This appears to happen when iterating through nodes in the wrap function.

Example scenario:
```js
const nodes = [
  { type: "element", name: "p", children: [...] },
  { type: "element", name: "p", children: [...] }
]

// After wrapping, an extra newline is added beyond the expected count
```

### Expected behavior

The wrap function should only add newlines between nodes and optionally at the beginning (if loose is true), but not add an extra one at the end that goes beyond the array bounds.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
