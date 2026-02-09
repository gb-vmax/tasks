# Bug Report

### Describe the bug

I'm experiencing an issue with markdown AST to string conversion where the output is missing the last element when processing arrays of nodes. The converted string appears to be incomplete and doesn't include all the content from the original markdown structure.

### Reproduction

```js
const nodes = [
  { type: 'text', value: 'Hello' },
  { type: 'text', value: ' ' },
  { type: 'text', value: 'World' }
];

const result = toString(nodes);
// Expected: "Hello World"
// Actual: "Hello " (missing "World")
```

When converting a markdown AST with multiple child nodes, only the first n-1 nodes are being processed. The last node in the array is consistently being skipped.

### Expected behavior

All nodes in the array should be converted to string and concatenated together. The complete text content should be returned without any elements being omitted.

### Additional context

This seems to affect any markdown structure with multiple sibling nodes. I noticed the output also sometimes has "undefined" prepended to it, which is also unexpected.

---
Repository: /testbed
